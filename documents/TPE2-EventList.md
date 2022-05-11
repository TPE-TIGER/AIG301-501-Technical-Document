# ThingsPro Edge Event List

Document Version: 1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-05-11 | document created. |



- List ThingsPro Edge support events

  ```
  curl https://127.0.0.1:8443/api/v1/events/profile -X GET -H "Content-Type:application/json" -H "mx-api-token:$(cat /var/thingspro/data/mx-api-token)" -k
  ```

  supported events are variable with ThingsPro Edge version, by above command, you can get available event list on the device.

- Example of ThingsPro Edge 2.2.0

```
{
    "data": {
        "origins": [
            ""
        ],
        "severities": [
            "info",
            "warning",
            "alert"
        ],
        "eventNames": [
            "DBIRTH has been sent",
            "MQTT Broker connected",
            "MQTT Broker disconnected",
            "NBIRTH has been sent",
            "Receive Control Command failed",
            "Receive Control Command successfully",
            "app crash",
            "app start",
            "app stop",
            "buffer active",
            "buffer clean",
            "buffer full",
            "buffer inactive",
            "buffer sending",
            "cellular attach fail",
            "cellular attached APN",
            "cellular no signal",
            "cellular set PIN code",
            "cellular set PIN code fail",
            "cellular signal good",
            "cellular signal low",
            "client connected",
            "client disconnected",
            "configuration reset",
            "configuration update failed",
            "configuration update success",
            "device connected",
            "device connection failed",
            "device disconnected",
            "device reboot",
            "device send properties fail",
            "device send telemetry",
            "device send telemetry fail",
            "external storage insert",
            "external storage remove",
            "external storage usage \u003e= 90%",
            "external storage usage \u003e= 95%",
            "function failed",
            "function recover",
            "link status change",
            "memory usage \u003e= 90%",
            "ota download cancel",
            "ota download completed",
            "ota download failed",
            "ota download resume",
            "ota download suspend",
            "server started",
            "slave device connected",
            "slave device failed",
            "software installation completed",
            "software installation failed",
            "system load 5 min \u003e= 1",
            "system load 5 min \u003e= 3",
            "system storage usage \u003e= 90%",
            "system storage usage \u003e= 95%",
            "time sync failed",
            "time sync success",
            "upgrade roll back completed",
            "uplink change",
            "user login fail"
        ],
        "categories": [
            "OPC-UA Server",
            "Sparkplug",
            "aws",
            "azure",
            "device setting",
            "modbus",
            "mqtt",
            "network",
            "store-forward",
            "system"
        ],
        "events": [
            {
                "id": 1,
                "enable": true,
                "severity": "alert",
                "category": "device setting",
                "event": "configuration update failed"
            },
            {
                "id": 2,
                "enable": false,
                "severity": "info",
                "category": "device setting",
                "event": "configuration update success"
            },
            {
                "id": 3,
                "enable": true,
                "severity": "warning",
                "category": "network",
                "event": "uplink change"
            },
            {
                "id": 4,
                "enable": true,
                "severity": "warning",
                "category": "device setting",
                "event": "time sync failed"
            },
            {
                "id": 5,
                "enable": false,
                "severity": "info",
                "category": "device setting",
                "event": "time sync success"
            },
            {
                "id": 6,
                "enable": true,
                "severity": "alert",
                "category": "network",
                "event": "cellular no signal"
            },
            {
                "id": 7,
                "enable": true,
                "severity": "warning",
                "category": "network",
                "event": "cellular signal low"
            },
            {
                "id": 8,
                "enable": false,
                "severity": "info",
                "category": "network",
                "event": "cellular signal good"
            },
            {
                "id": 9,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "system storage usage \u003e= 90%"
            },
            {
                "id": 10,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "system storage usage \u003e= 95%"
            },
            {
                "id": 11,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "system load 5 min \u003e= 1"
            },
            {
                "id": 12,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "system load 5 min \u003e= 3"
            },
            {
                "id": 13,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "memory usage \u003e= 90%"
            },
            {
                "id": 18,
                "enable": false,
                "severity": "info",
                "category": "azure",
                "event": "device connected"
            },
            {
                "id": 19,
                "enable": true,
                "severity": "warning",
                "category": "azure",
                "event": "device disconnected"
            },
            {
                "id": 20,
                "enable": true,
                "severity": "alert",
                "category": "azure",
                "event": "device connection failed"
            },
            {
                "id": 21,
                "enable": true,
                "severity": "alert",
                "category": "azure",
                "event": "device send properties fail"
            },
            {
                "id": 22,
                "enable": true,
                "severity": "alert",
                "category": "azure",
                "event": "device send telemetry fail"
            },
            {
                "id": 23,
                "enable": true,
                "severity": "warning",
                "category": "store-forward",
                "event": "buffer active"
            },
            {
                "id": 24,
                "enable": false,
                "severity": "info",
                "category": "store-forward",
                "event": "buffer inactive"
            },
            {
                "id": 25,
                "enable": false,
                "severity": "info",
                "category": "store-forward",
                "event": "buffer sending"
            },
            {
                "id": 26,
                "enable": false,
                "severity": "info",
                "category": "store-forward",
                "event": "buffer clean"
            },
            {
                "id": 27,
                "enable": true,
                "severity": "alert",
                "category": "store-forward",
                "event": "buffer full"
            },
            {
                "id": 28,
                "enable": false,
                "severity": "info",
                "category": "mqtt",
                "event": "device connected"
            },
            {
                "id": 29,
                "enable": true,
                "severity": "warning",
                "category": "mqtt",
                "event": "device disconnected"
            },
            {
                "id": 30,
                "enable": true,
                "severity": "alert",
                "category": "mqtt",
                "event": "device connection failed"
            },
            {
                "id": 31,
                "enable": true,
                "severity": "alert",
                "category": "mqtt",
                "event": "device send telemetry fail"
            },
            {
                "id": 37,
                "enable": true,
                "severity": "warning",
                "category": "modbus",
                "event": "configuration update success"
            },
            {
                "id": 38,
                "enable": true,
                "severity": "warning",
                "category": "modbus",
                "event": "configuration update failed"
            },
            {
                "id": 39,
                "enable": false,
                "severity": "info",
                "category": "modbus",
                "event": "slave device connected"
            },
            {
                "id": 40,
                "enable": true,
                "severity": "alert",
                "category": "modbus",
                "event": "slave device failed"
            },
            {
                "id": 41,
                "enable": false,
                "severity": "info",
                "category": "modbus",
                "event": "function recover"
            },
            {
                "id": 42,
                "enable": true,
                "severity": "warning",
                "category": "modbus",
                "event": "function failed"
            },
            {
                "id": 48,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "device reboot"
            },
            {
                "id": 49,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "user login fail"
            },
            {
                "id": 50,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "app stop"
            },
            {
                "id": 51,
                "enable": false,
                "severity": "info",
                "category": "system",
                "event": "app start"
            },
            {
                "id": 52,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "app crash"
            },
            {
                "id": 53,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "ota download failed"
            },
            {
                "id": 54,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "ota download suspend"
            },
            {
                "id": 55,
                "enable": false,
                "severity": "info",
                "category": "system",
                "event": "ota download resume"
            },
            {
                "id": 56,
                "enable": false,
                "severity": "info",
                "category": "system",
                "event": "ota download completed"
            },
            {
                "id": 57,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "ota download cancel"
            },
            {
                "id": 58,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "software installation failed"
            },
            {
                "id": 59,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "upgrade roll back completed"
            },
            {
                "id": 60,
                "enable": false,
                "severity": "info",
                "category": "system",
                "event": "software installation completed"
            },
            {
                "id": 61,
                "enable": false,
                "severity": "info",
                "category": "system",
                "event": "external storage insert"
            },
            {
                "id": 62,
                "enable": false,
                "severity": "info",
                "category": "system",
                "event": "external storage remove"
            },
            {
                "id": 63,
                "enable": false,
                "severity": "info",
                "category": "network",
                "event": "cellular attached APN"
            },
            {
                "id": 64,
                "enable": true,
                "severity": "warning",
                "category": "network",
                "event": "cellular attach fail"
            },
            {
                "id": 65,
                "enable": false,
                "severity": "info",
                "category": "network",
                "event": "cellular set PIN code"
            },
            {
                "id": 66,
                "enable": true,
                "severity": "warning",
                "category": "network",
                "event": "cellular set PIN code fail"
            },
            {
                "id": 73,
                "enable": true,
                "severity": "warning",
                "category": "OPC-UA Server",
                "event": "configuration update success"
            },
            {
                "id": 74,
                "enable": true,
                "severity": "warning",
                "category": "OPC-UA Server",
                "event": "configuration update failed"
            },
            {
                "id": 75,
                "enable": false,
                "severity": "info",
                "category": "OPC-UA Server",
                "event": "server started"
            },
            {
                "id": 76,
                "enable": true,
                "severity": "alert",
                "category": "OPC-UA Server",
                "event": "client connected"
            },
            {
                "id": 77,
                "enable": true,
                "severity": "warning",
                "category": "OPC-UA Server",
                "event": "client disconnected"
            },
            {
                "id": 78,
                "enable": true,
                "severity": "warning",
                "category": "system",
                "event": "external storage usage \u003e= 90%"
            },
            {
                "id": 79,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "external storage usage \u003e= 95%"
            },
            {
                "id": 80,
                "enable": true,
                "severity": "alert",
                "category": "system",
                "event": "configuration reset"
            },
            {
                "id": 1000,
                "enable": false,
                "severity": "info",
                "category": "Sparkplug",
                "event": "configuration update success"
            },
            {
                "id": 1001,
                "enable": true,
                "severity": "warning",
                "category": "Sparkplug",
                "event": "configuration update failed"
            },
            {
                "id": 1002,
                "enable": false,
                "severity": "info",
                "category": "Sparkplug",
                "event": "MQTT Broker connected"
            },
            {
                "id": 1003,
                "enable": true,
                "severity": "alert",
                "category": "Sparkplug",
                "event": "MQTT Broker disconnected"
            },
            {
                "id": 1004,
                "enable": false,
                "severity": "info",
                "category": "Sparkplug",
                "event": "NBIRTH has been sent"
            },
            {
                "id": 1005,
                "enable": false,
                "severity": "info",
                "category": "Sparkplug",
                "event": "DBIRTH has been sent"
            },
            {
                "id": 1006,
                "enable": false,
                "severity": "info",
                "category": "Sparkplug",
                "event": "Receive Control Command successfully"
            },
            {
                "id": 1007,
                "enable": true,
                "severity": "alert",
                "category": "Sparkplug",
                "event": "Receive Control Command failed"
            },
            {
                "id": 1050,
                "enable": false,
                "severity": "info",
                "category": "aws",
                "event": "device connected"
            },
            {
                "id": 1051,
                "enable": true,
                "severity": "warning",
                "category": "aws",
                "event": "device disconnected"
            },
            {
                "id": 1052,
                "enable": true,
                "severity": "alert",
                "category": "aws",
                "event": "device connection failed"
            },
            {
                "id": 1053,
                "enable": true,
                "severity": "alert",
                "category": "aws",
                "event": "device send telemetry"
            },
            {
                "id": 2000,
                "enable": true,
                "severity": "warning",
                "category": "network",
                "event": "link status change"
            }
        ]
    }
}
```



