import json

def tpedm_command_message(name, step, response):
    message = general_fields(name, step)
    if (isinstance(response, str)):
        message["content"] = json.loads(response)
    else:
        print(response)
    
    return message

def swoftware_scan_message(name, step, sw_update_scan_flag, clientid=None, clientProfile=None, softwarePackage=None):
    message = general_fields(name, step)
    message["content"] = {}
    message["content"]["sw_update_scan_flag"] = sw_update_scan_flag
    
    if step == "found":
        message["content"]["clientid"] = clientid
        message["content"]["clientProfile"] = clientProfile
        message["content"]["softwarePackage"] = softwarePackage
    
    return message
    

def browser_connection_message(name, step):
    message = general_fields(name, step)
    
    return message

def device_connection_message(name, step, clientid, connection_status):
    message = general_fields(name, step)
    message["content"] = {}
    message["content"]["clientid"] = clientid
    message["content"]["connection_status"] = connection_status
    
    return message


def general_fields(name, step):
    message = {
        "name": name,
        "step": step
    }
    
    return message