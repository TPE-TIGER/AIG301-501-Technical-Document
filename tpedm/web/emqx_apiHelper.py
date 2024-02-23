#!/usr/bin/python
import requests, time
import datetime

class EMQX_API_Helper():
    def __init__(self, config):
        self.url = config["EMQX_Manage_API"]["soureURI"]
        self.headers = config["EMQX_Manage_API"]["headers"]
    
    def get_clientid(self, clientid):
        url1 = self.url + "clients/" + clientid
        try:
            resp = requests.get(url=url1, headers=self.headers)
        except (Exception) as error:
            print("ERROR" + str(error))
            return False, error

        return True, resp.content.decode("utf-8") 
    
    def emqx_post_message(self, clientid, messagePayload):
        url1 = self.url + "mqtt/publish"
        payload = {
                "topic": "/tpedm/" + clientid + "/input",
                "qos": 1, 
                "clientid": clientid,
                "payload": messagePayload
            }
        try:
            print("[INFO] emqx: " + str(messagePayload))
            resp = requests.post(url=url1, headers=self.headers, json=payload)
        except (Exception) as error:
            print("ERROR" + str(error))
            return False, error

        return True, resp.content.decode("utf-8") 
    
    def publish_dm_request_message(self, clientid, actionName, actionDesc, path, method, request_content, wait_sec=0):
        time.sleep(wait_sec)
        current_date_and_time = datetime.datetime.now()
        expired = current_date_and_time + datetime.timedelta(hours=1)
        request_id = int(time.time())
        messagePayload = {
            "path": path,
            "method": method.upper(),
            "headers": [
                {
                    "request-expired-time": str(expired)
                },
                {
                    "request-id": str(request_id)
                }
            ],
            "requestBody": request_content
        }             
        
        status, message = self.emqx_post_message(clientid, messagePayload)
        if status:
            return -1
        
        return request_id
    
    
    
    


    

    
 
    