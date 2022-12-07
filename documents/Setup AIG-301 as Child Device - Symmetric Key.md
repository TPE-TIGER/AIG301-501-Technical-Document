# Setup AIG-301 as Child Device (Symmetric Key)

Document Version: V1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-12-07 | document created. |

### 1. Architecture

​		<img src="https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-architecture-key.JPG" style="zoom:50%;" />

#### 1.1 IoT-Gateway

IoT-Gateway is a virtual machine (Ubuntu 20.04) on Azure Cloud, which contains Azure IoT Edge v1.4 . In order to allow child device connect with, the IoT-Gateway need

- A valid FQDN, iot-gateway.thingspro.io (for example)
- Open inbound firewall ports: 8883, 443, 5671, 22

#### 1.2 MOXA-IVR-01

MOXA-IVR-01 is one Moxa IIoT Gateway such as AIG-301, locates at OT field. Azure IoT Device running on MOXA-IVR-01, connects to IoT-Gateway, and authenticate with Azure IoT Hub via Symmetric Key.



------

### 2. Tasks on Azure IoT Hub

##### 2.1 Create IoT Edge: iot-gateway

- On Azure IoT Hub, find IoT Edge from menu, then, add a IoT Edge device (iot-gateway).

- After creation task complete, add 2 message routes for iot-gateway to allow iot-gateway function as transparent gateway.

  ![](https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-2-msg-route.JPG)

**Reference**: https://learn.microsoft.com/en-us/azure/iot-edge/how-to-create-transparent-gateway?view=iotedge-2020-11&preserve-view=true&tabs=iotedge#deploy-edgehub-and-route-messages 



##### 2.3 Create IoT Device: moxa-ivr-01

- On Azure IoT Hub, find Devices from menu, then, add a Device (moxa-ivr-01)
- Select "Symmetric Key" as Authentication type
- Select "iot-gateway" as Parent device



------

### 3. Tasks on IoT-Gateway

##### 3.1 Install Azure IoT Edge v1.4

**Reference**: https://learn.microsoft.com/en-us/azure/iot-edge/how-to-provision-single-device-linux-symmetric?view=iotedge-1.4&tabs=azure-portal%2Cubuntu#install-iot-edge

##### 3.2 Prepare for child device connection

To allow child device be able to connect with, the IoT-Gateway must have:

- A valid FQDN, iot-gateway.thingspro.io (for example)

  ​	Azure IoT Device (child device) only support connecting to a valid FQDN gateway.

- Open inbound firewall ports

  - 8883, 443, 5671: for child device connection and communication
  - 22: for you to setup

- Create downstream X.509 chain certificate

  - On IoT-Gateway virtual machine, login ssh console as root (sudo su), and run below commands:

    ```
    wget https://thingspro.blob.core.windows.net/resource/document/E-ON/openssl.cnf
    wget https://thingspro.blob.core.windows.net/resource/document/E-ON/create.sh
    chmod 755 ./create.sh
    ./create.sh
    ```

    These commands will generate **aie.key**, **aie.crt**, **aieChain.crt**, these are what we need, please copy them to IoT-Gateway filesystem, "/home/moxa/iotedge-cert" (for example).

##### 3.3 Start Azure IoT Edge, connect to Azure IoT Hub

- Edit /etc/aziot/config.toml, replace below keys with values
  - hostname = "iot-gateway.thingspro.io"
  - trust_bundle_cert = "file path to aieChain.crt"
  - [provisioning] / source = "manual"
  - [provisioning] / connection_string = "COPY iot-gateway connection string from Azure IoT Hub"
  - [edge_ca] / cert = "file path to aie.crt"
  - [edge_ca] / pk = "file path to aie.key"

Example:	

```
hostname = "iot-gateway.thingspro.io"
trust_bundle_cert = "file:///home/moxa/iotedge-cert/aieChain.crt"

[provisioning]
source = "manual"
connection_string = "HostName=TP............................sKey=+hBZ...arV0tSQGQ="

[edge_ca]
cert = "file:///home/moxa/iotedge-cert/aie.crt"               
pk = "file:///home/moxa/iotedge-cert/aie.key"              
```

- Start Azure IoT Edge

```
iotedge config apply
```



------

### 4. Tasks on MOXA-IVR-01

##### 4.1 Time Sync

- Login to AIG-301 Web admin, on System Settings / General, make sure the time zone and time are correct.

  <img src="https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-time-sync.JPG" style="zoom:67%;" />



##### 4.2 Verify IoT-Gateway X.509 certificate

- Login to AIG-301 SSH console, run below command to retrieve IoT-Gateway's X.509 certificate

  ```
  echo | openssl s_client -connect iot-gateway.thingspro.io:8883 2>/dev/null | openssl x509 -text
  ```

  From output, verify below keys and values are matched with your setting

  - Issuer: CN = IoT Edge CA
  - Subject: CN = iot-gateway.thingspro.io

##### 4.3 Setup and start Azure IoT Device

- Login to AIG-301 Web admin, on Azure IoT Device, click setting icon

![](https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-aid-2.JPG)

- Select Authentication Type：Symmetric Key, and input 

  | Key               | Value                                                        | Desc                                                         |
  | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | Connection String | HostName=TPE-TIGER.azure-devices.net;DeviceId=moxa-ivr-01;SharedAccessKey=r5ctNdN.....UUJ0=GatewayHostName=iot-gateway.thingspro.io | You shall change  Azure IoT Hub host.domain by your case     |
  | Trusted Root CA   | Import file: aieChain.crt                                    | Trusted Root CA be used to verify the X.509 certificate sending from iot-gateway.thingspro.io |
  
- Save it to start Azure IoT Device.

##### ![](https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-2-aid-connect.JPG)



