# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms, disconnect
import web_dbHelper, emqx_apiHelper, tpc_apiHelper, socket_message
import json, _thread

# --Define global variables------------------------------------------------------- #
_config_content = None
_socketPath = '/api/rtmessage'
_web_db = None 
_emqx = None
_sw_repo = None
_sw_update_scan_flag = 0

app = Flask(__name__)
app.secret_key = 'my secret key'
async_mode = None
_device_connection_room = "device_con_status"
_software_update_room = "software_update"
_submit_command_room = "submit_command"
socketio = SocketIO(app, path=_socketPath, cors_allowed_origins='*', async_mode=async_mode)

# -- Restful API------------------------------------------------------- #

# --Webhook, called from EMQX MQTT Broker when device:----------------------- #
#            - connected
#            - disconnect
#            - send DM response to topic: /tpedm/+/output
# --------------------------------------------------------------------------- #
@app.route('/api/emqx/hook', methods=['POST'])
def api_emqx_hook():    
    message = request.json
    print("[INFO] hook: " + json.dumps(message))
    clientid = None
    
    # Verify clientid in database. Create clientid if not exist in database    
    if "clientid" in message:
        clientid = message["clientid"]
    elif "topic" in message:
        if message["topic"].startswith("/tpedm"):
            clientid = message["from_client_id"]
        else:
            print("[INFO] Skip webhook message, topic:" + message["topic"])
            return "fail"
    else:
        print("[INFO] Unknow message. Exit webhook.")
        return "fail"
    
    clientidList, error = _web_db.get_clientid_profile(clientid)
    if error:
        print("[ERROR] Fail on access DB. Exit webhook.")  
        return "fail"
    if len(clientidList)==0:
        print("[ERROR] Can't find client id on dababase. Exit webhook. clientid: " + clientid) 
        return "fail"
    
    # Process message by action type
    if message["action"] == "client_connected":         
        _web_db.update_clientid_profile_connection_status(message["clientid"], True, message["connected_at"])
        
        emit_message = socket_message.device_connection_message("device connection", "connected", message["clientid"], 1)
        socketio.emit("onMessage", {"data": emit_message})
                
        # At everytime device connected, tpedm send DM request to device to ask for sending device profile back
        try:
            _thread.start_new_thread(_emqx.publish_dm_request_message, (message["clientid"], "sys-get-device-profile", None, "/device/general", "GET", None, 5) )
        except:
            print ("[ERROR] unable to start thread (sys-get-device-profile)")
            
        return "ok"
        
    elif message["action"] == "client_disconnected":
        _web_db.update_clientid_profile_connection_status(message["clientid"], False, None)
        
        emit_message = socket_message.device_connection_message("device connection", "disconnected", message["clientid"], 0)
        socketio.emit("onMessage", {"data": emit_message})
        
        return "ok"
        
    elif message["action"] == "message_publish":
        contentMessage = json.loads(message["payload"])
        if message["topic"].startswith("/tpedm"):
            if message["topic"].endswith("/output"):         # Received client's DM response                
                clientid = message["from_client_id"]
                
                # --- On Received GET /device/general command
                if "data" in contentMessage["payload"]:
                    if "type" in contentMessage["payload"]["data"]:
                        data = contentMessage["payload"]["data"]
                        if data["type"] == "general":
                            status, result = _web_db.update_clientid_profile(clientid, data["modelName"], data["serialNumber"], data["hostName"],data["thingsproVersion"], data["firmwareVersion"], data["biosVersion"])
                           
                # --- On Received All command    
                emit_message = socket_message.tpedm_command_message("tpedm command", "output", message["payload"])
                socketio.emit("onMessage", {"data": emit_message})
                                
            else:
                #print("skip non-support topic")
                return "OK"
        else:
            #print("skip non-support topic")
            return "OK"
    else:
        #print("skip non-support action")
        return "OK"
        
    return "OK"

# --Submit a DM request to EMQX MQTT Broker and to specific TPE device (clientid)----- #
# postData schema example
# {
#   "path": "/system/reboot",
#   "method": "PUT",
#   "headers": [
#     {
#       "request-expired-time": "2022-04-17 13:07:07"
#     },
#     {
#       "request-id": "1650172027040"
#     }
#   ],
#   "requestBody": {
#     "now": true
#   }
# }
# --------------------------------------------------------------------------- #
@app.route('/api/emqx/clients/<string:clientid>/message', methods=['POST'])
def api_emqx_message_post(clientid):
    result = {}
    messagePayload = request.json  
    try:
        _thread.start_new_thread(_emqx.emqx_post_message, (clientid, messagePayload) )
        result["status"] = True
        result["data"] = "OK"        
    except:
        print ("[ERROR]  unable to start thread") 
        result["status"] = False
        result["data"] = "Error: unable to start thread"
        
    return json.dumps(result)    
    
# --GET TPE device connection data from EMQX MQTT Broker-------------------------------- #
@app.route('/api/emqx/clients/<string:clientid>', methods=['GET'])
def api_emqx_get_clientid(clientid):
    result = {}
    status, content = _emqx.get_clientid(clientid)
    if (status):
        result["status"] = True
        result["data"] = json.loads(content)
        return json.dumps(result)
    else:
        result["status"] = False
        return json.dumps(result)
        

# --Get TPE device list from database ---------------------------------------- #
# Resonse schema
# { 
#   "data" : [{
#       "clientid":"",
#       "username":"",
#       "model_name":"",
#       "serial_number":"",
#       "host_name":"",
#       "tpe_version":"",
#       "firmware_version": ""
#       "bios_version": "",
#       "connection_status":"",
#       "connection_status_updated_at":""
#   }]
# }
# --------------------------------------------------------------------------- #
@app.route('/api/device', methods=['GET'])
def api_get_devices():
    result = {}
    clientidList, error = _web_db.get_clientid_profile(None)
    if error:
        result["status"] = False
        return json.dumps(result)
    else:
        result["status"] = True
        result["data"] = clientidList
        return json.dumps(result)

# --Get One TPE device by clientid from database ---------------------------------------- #
# Resonse schema
# { 
#   "data" : {
#       "clientid":"",
#       "username":"",
#       "model_name":"",
#       "serial_number":"",
#       "host_name":"",
#       "tpe_version":"",
#       "firmware_version": ""
#       "bios_version": "",
#       "connection_status":"",
#       "connection_status_updated_at":""
#   }
# }
# --------------------------------------------------------------------------- #
@app.route('/api/device/<string:clientid>', methods=['GET'])
def api_get_device(clientid):
    result = {}
    clientidList, error = _web_db.get_clientid_profile(clientid)
    if error:
        result["status"] = False
        return json.dumps(result)
    else:
        result["status"] = True
        result["data"] = clientidList[0]
        return json.dumps(result)

# -- Create One TPE device (on database) ---------------------------------------- #
# postData schema
# { 
#   "clientid": "", 
#   "username": "",
#   "password": ""
# }
# --------------------------------------------------------------------------- #
@app.route('/api/device', methods=['POST'])
def api_create_device():
    result = {}
    content = request.json
    status, message = _web_db.create_clientid_profile(content["clientid"], content["username"], content["password"])    
        
    result["status"] = status
    result["data"] = message
    return json.dumps(result)

# --DELETE One TPE Device (from database) ---------------------------------------- #
@app.route('/api/device/<string:clientid>', methods=['DELETE'])
def api_delete_device(clientid):
    result = {}    
    status, message = _web_db.delete_clientid_profile(clientid)
    result["status"] = status
    result["data"] = message
    return json.dumps(result)

# --Get Operation Category ---------------------------------------- #
# Resonse schema
# { 
#   "data" : [{
#       "id":1,
#       "name":""
#   }]
# }
# --------------------------------------------------------------------------- #
@app.route('/api/operation/category', methods=['GET'])
def api_get_operation_category():
    result = {}
    categoryList, error = _web_db.get_operation_category()
    if error:
        result["status"] = False
        return json.dumps(result)
    else:
        result["status"] = True
        result["data"] = categoryList
        return json.dumps(result)

# --Get Operation command by categoryid ---------------------------------------- #
# Resonse schema
# { 
#   "data" : [{
#       "id":1,
#       "categoryid": 1
#       "name":"",
#       "command": ""
#   }]
# }
# --------------------------------------------------------------------------- #
@app.route('/api/operation', methods=['GET'])
def api_get_operation_by_category():
    result = {}
    categoryid = request.args.get('categoryid')
    operationList, error = _web_db.get_operation_by_category(categoryid)
    if error:
        result["status"] = False
        return json.dumps(result)
    else:
        result["status"] = True
        result["data"] = operationList
        return json.dumps(result)

# --Run Software Scan ---------------------------------------- #
@app.route('/api/device/checkUpdate', methods=['PUT'])
def api_run_devices_check_update():
    result = {}
    # run check software upgrade at background
    try:
        _thread.start_new_thread(ask_check_software_update)
        result["status"] = True
        result["data"] = "" 
    except:
        result["status"] = False
        result["data"] = "create check software scan process fail" 
    
    return json.dumps(result)

# --Socket IO ---------------------------------------- #
@socketio.on('join', namespace='')
def join(in_message):
    join_room(in_message['room'])
    emit_message = socket_message.browser_connection_message("browser connection", "join room")
    socketio.emit("onMessage", {"data": emit_message})
    #print('[INFO] Client join room. Client: ' + request.sid + ', roomId: ' + in_message['room'])
    
@socketio.on('leave', namespace='')
def leave(in_message):
    leave_room(in_message['room'])
    emit_message = socket_message.browser_connection_message("browser connection", "leave room")
    socketio.emit("onMessage", {"data": emit_message})
    #print('[INFO] Client leave room. Client: ' + request.sid + ', roomId: ' + in_message['room'])

@socketio.on('disconnect_request', namespace='')
def disconnect_request():
    emit_message = socket_message.browser_connection_message("browser connection", "disconnect request")
    socketio.emit("onMessage", {"data": emit_message})
    disconnect()

@socketio.on('my_ping', namespace='')
def ping_pong():
    emit('my_pong')
    
@socketio.on('connect', namespace='')
def send_connect_welcome():
    emit_message = socket_message.browser_connection_message("browser connection", "connected")
    socketio.emit("onMessage", {"data": emit_message})
    print('[INFO] Client connect. Client: ' + request.sid)

@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('[INFO] Client disconnected. Client: ' + request.sid)
    

# --Internal Funciton------------------------------------------------------- #
# -- Function to handle new software found for a Device -------------- #
def handle_new_software_found(clientid, package):    
    print("[INFO] Find new package: " + json.dumps(package))
    try:
        profileList, error = _web_db.get_clientid_profile(clientid)
        emit_message = socket_message.swoftware_scan_message("software scan", "found", _sw_update_scan_flag, clientid, profileList[0], package)
        socketio.emit("onMessage", {"data": emit_message})
    except Exception as e:
        print("[ERROR] " + str(e))
    

# -- A thread to Check any new software on all devices----------------------- #
# 1. Call TPC SW Repo
# 2. Update new package into datbase
# 3. Push new package message via Socket IO
# --------------------------------------------------------------------------- #
def ask_check_software_update():
    global _sw_update_scan_flag
    global _web_db
    global _sw_repo   
   
    _sw_update_scan_flag = 1 
    emit_message = socket_message.swoftware_scan_message("software scan", "scan...", _sw_update_scan_flag)
    socketio.emit("onMessage", {"data": emit_message})   
    print("[INFO] ask check software scan")
    
    # Check all devices by version data stored at database
    deviceList, error = _web_db.get_clientid_profile()
    total_devices = len(deviceList)
    pos = 1
    if not error:
        for device in deviceList:
            step = str(pos) + "/" + str(total_devices) 
            emit_message = socket_message.swoftware_scan_message("software scan", "scan: " + step, _sw_update_scan_flag,)
            socketio.emit("onMessage", {"data": emit_message})  
            
            if (device["firmware_version"] != None) and (device["model_name"] != None):
                package = _sw_repo.scan_mil_package(device["firmware_version"], device["model_name"])
                if package != None:
                    handle_new_software_found(device["clientid"], package)
                else:
                    package = _sw_repo.scan_tpe_package(device["firmware_version"], device["tpe_version"], device["model_name"])
                    if package != None:
                        handle_new_software_found(device["clientid"], package)
            pos = pos + 1
    
    _sw_update_scan_flag = 0
    emit_message = socket_message.swoftware_scan_message("software scan", "Check Update", _sw_update_scan_flag)
    socketio.emit("onMessage", {"data": emit_message}) 
    print("[INFO] completed check software scan")           
            
# -- Web UI HTML Page ------------------------------------------ #        
@app.route('/')
def home():
    return render_template('devices.html', socketPath=_socketPath + "/socket.io", zoomName=_device_connection_room, async_mode=socketio.async_mode) 

@app.route('/index.html')
def index_page():
    return home()

@app.route('/devices.html')
def devices_page():
    return home()

@app.route('/software-update.html')
def software_update():
    return render_template('software-update.html', socketPath=_socketPath + "/socket.io", zoomName=_software_update_room, async_mode=socketio.async_mode) 

@app.route('/device-register.html')
def device_register_page():
    return render_template('device-register.html') 

@app.route('/view-profile')
def view_device_profile():
    clientid = request.args.get('clientid')
    return render_template('view-profile.html', clientid=clientid) 

@app.route('/submit-command')
def submit_device_command():
    clientid = request.args.get('clientid')
    return render_template('submit-command.html', clientid=clientid, socketPath=_socketPath + "/socket.io", zoomName=_submit_command_room, async_mode=socketio.async_mode)



# ---------------------------------------------------------- #
# Load Configuration
config_file = "data//config.json"
_config_content = json.load(open(config_file,"r",encoding="utf-8"))
_web_db = web_dbHelper.WEB_DB(_config_content, 2, 10)
_emqx = emqx_apiHelper.EMQX_API_Helper(_config_content)
_sw_repo = tpc_apiHelper.SW_Repo_Helper(_config_content)

if __name__ == '__main__':
    socketio.run(app, host=_config_content["web"]["host"], port=_config_content["web"]["port"], debug=True, use_reloader=True)
    
