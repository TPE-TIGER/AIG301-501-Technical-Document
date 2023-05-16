# Invoke ThingsPro Edge Restful API from MQTT Server

Document Version: V1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-02-10 | document created. |



### Purpose

When ThingsPro Edge MQTT client connected with MQTT server, apart from send over telemetry message, it also allows you to invoke ThingsPro Edge Restful API from MQTT server and get response back asynchrony. 

Many customers enjoy this feature for device management (such as turn on/off service, adjust configurations) and actuator control by write data to Modbus slave device remotely on cloud.

##### Related documents：

- ThingsPro Edge Restful API.

  

### 1. Feature Enable

On ThingsPro Edge MQTT client setting page, you shall

- Enable Invoke Device Restful API from MQTT Server

- Define name of "Input Topic". MQTT client will receive message (API Request) from this topic.

- Define name of "Out Topic". MQTT client will send out message (API Response) to this topic.

  
<p align="center" width="100%"><img src="https://thingspro.blob.core.windows.net/resource/document/mqtt/mqtt-dm.jpg" width="960" /></p>


- By above configuration, MQTT client created 2 MQTT topics with MQTT Server, and expect to receive API request on **topic:/devices/1/request**

   <p align="center" width="100%"><img src="https://thingspro.blob.core.windows.net/resource/document/mqtt/mqtt-dm2.jpg" width="640" /></p>


### 2. Device Configuration from Cloud
#### 2.1 Publish API Request from Cloud Program

Now, you are ready to invoke ThingsPro Edge's Restful API on your cloud program. For example, publish below message to **topic:/devices/1/request** will turn on device's SSH service. 

```
{
    "path": "/system/sshserver",
    "method": "PUT",
    "headers": [
        {
            "request-expired-time": "2020-11-12 11:45:26"
        },
        {
            "request-id": "1"
        }
    ],
    "requestBody": {
        "enable": true,
        "port": 22
    }
}
```

| No   | Field                         |                                                              |
| ---- | ----------------------------- | ------------------------------------------------------------ |
| 1    | path                          | The end point of ThingsPro Edge Restful API you would like to invoke |
| 2    | method                        | The method name associated with the end point.               |
| 3    | header - request-expired-time | The expiration time of this invocation. <br />UTC and ISO-8601. <br />MQTT client will skip request API if assigned "request-expired-time" is invalid.|
| 4    | header - request-id           | The unique Id of this invocation. This Id will be append into API response content. |
| 5    | requestBody                   | The payload of this Restful API if any.                      |



#### 2.2 Receive API Response on Cloud Program

MQTT client executes the request and publish result into **topic:/devices/1/response**. Cloud Program shall subscribe this topic to receive API response.

Below is payload example:

```
{
  "request-id": "1",
  "state": 200,
  "payload": "{\"data\":{\"type\":\"general\",\"description\":\"1\",\"hostName\":\"Moxa\",\"modelName\":\"UC-8100A-ME-T-LX\",\"deviceType\":\"gateway\",\"serialNumber\":\"TAICB1046773\",\"firmwareVersion\":\"1.3.1\",\"thingsproVersion\":\"1.1.0-594\",\"cpu\":\"ARMv7Processorrev2(v7l)\",\"memorySize\":1055838208,\"disk\":[{\"name\":\"System\",\"mount\":\"/\",\"device\":\"/dev/root\",\"total\":6827344896,\"free\":4880628736,\"used\":1659873280,\"percent\":25.37837731628948,\"tags\":{\"used\":\"systemDiskUsed\",\"free\":\"systemDiskFree\",\"percent\":\"systemDiskPercent\"}}],\"lastBootTime\":\"2019-12-20T11:31:20+08:00\"}}"
}
```

| No   | Field      |                                             |
| ---- | ---------- | ------------------------------------------- |
| 1    | request-id | The unique Id which place at request header |
| 2    | status     | Restful API execution result                |
| 3    | payload    | Restful API execution output.<br />String.  |

### 3. Control Slave Device from Cloud
#### 3.1 Publish Write Tag API Request from Cloud Program
Say there is one modbus tcp slave device, my_fan, connected with AIG device, and I would like to adjust it rpm (revolutions per minute) to 100.2. So, I can publish below message to **topic:/devices/1/request**.
```
{
    "path": "/modbusmaster/operate/direct-write-tag",
    "method": "PUT",
    "headers": [
        {
            "request-expired-time": "2020-11-12 11:45:26"
        },
        {
            "request-id": "1"
        }
    ],
    "requestBody": {
        "prvdName": "modbus_tcp_master",
        "srcName": "my_fan",
        "tagName": "rpm",
        "dataType": "float",
        "dataValue": 100.2
    }
}
```
#### 3.2 Receive Write Tag API Response on Cloud Program
MQTT client then, transfer this request to Modbus Master, waiting execution result, and publish result into **topic:/devices/1/response**. Cloud Program shall subscribe this topic to receive API response.
