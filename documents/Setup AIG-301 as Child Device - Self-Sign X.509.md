# Setup AIG-301 as Child Device (Self-Sign X.509)

Document Version: V1.1

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.1     | 2023-06-09 | add troubleshooting |

### 1. Architecture

​		<img src="https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-architecture.JPG" style="zoom:50%;" />

#### 1.1 IoT-Gateway

IoT-Gateway is a virtual machine (Ubuntu 20.04) on Azure Cloud, which contains Azure IoT Edge v1.4 . In order to allow child device connect with, the IoT-Gateway need

- A valid FQDN, iot-gateway.thingspro.io (for example)
- Open inbound firewall ports: 8883, 443, 5671, 22

#### 1.2 MOXA-IVR-01

MOXA-IVR-01 is one Moxa IIoT Gateway such as AIG-301, locates at OT field. Azure IoT Device running on MOXA-IVR-01, connects to IoT-Gateway, and authenticate with Azure IoT Hub via Self-Sign X.509 certificate.



------

### 2. Tasks on Azure IoT Hub

##### 2.1 Create IoT Edge: iot-gateway

- On Azure IoT Hub, find IoT Edge from menu, then, add a IoT Edge device (iot-gateway).

- After creation task complete, add 2 message routes for iot-gateway to allow iot-gateway function as transparent gateway.

  ![](https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-2-msg-route.JPG)

**Reference**: https://learn.microsoft.com/en-us/azure/iot-edge/how-to-create-transparent-gateway?view=iotedge-2020-11&preserve-view=true&tabs=iotedge#deploy-edgehub-and-route-messages 



##### 2.2 Create X.509 certificate for moxa-ivr-01

Login as root (sudo su) on an Ubuntu virtual machine with openssl package (you can use IoT-Gateway virtual machine)...

- Create private key for moxa-ivr-01 device

  ```
  openssl genrsa -out moxa-ivr-01.key 2048
  ```

- Generate certificate sign request for moxa-ivr-01 device

  ```
  openssl req -new -key moxa-ivr-01.key -out moxa-ivr-01.csr
  ```

  You need to input some meta-data, such as country, state....; 

  **You MUST input 'moxa-ivr-01' on Common Name.** Azure IoT Hub will verify if Common Name value match with Device Name.

  Don't apply password, just type Enter.

- Use self-private key to sign moxa-ivr-01 certificate

  ```
  openssl x509 -req -days 365 -in moxa-ivr-01.csr -signkey moxa-ivr-01.key -out moxa-ivr-01.crt
  ```

- Retrieve thumbprint of moxa-ivr-01.crt

  Open moxa-ivr-01.crt on windows OS to retrieve thumbprint.

  <img src="https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-2-thumb.JPG" style="zoom:50%;" />

##### 2.3 Create IoT Device: moxa-ivr-01

- On Azure IoT Hub, find Devices from menu, then, add a Device (moxa-ivr-01)
- Select "X.509 Self-Signed" as Authentication type
- Input Primary & Secondary Thumbprint = **thumbprint you retrieve from above step**
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

![](https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-aid.JPG)

- Select Authentication Type：X.509 Certificate, and input 

  | Key               | Value                                                        | Desc                                                         |
  | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | Connection String | HostName=TPE-TIGER.azure-devices.net;DeviceId=moxa-ivr-01;x509=true;GatewayHostName=iot-gateway.thingspro.io | You shall change  Azure IoT Hub host.domain by your case     |
  | X.509 Certificate | Import file: moxa-ivr-01.cer                                 | moxa-ivr-01 X.509 certificate                                |
  | Private Key       | Import file: moxa-ivr-01.key                                 | moxa-ivr-01 private key                                      |
  | Trusted Root CA   | Import file: aieChain.crt                                    | Trusted Root CA be used to verify the X.509 certificate sending from iot-gateway.thingspro.io |

- Save it to start Azure IoT Device.

##### ![](https://thingspro.blob.core.windows.net/resource/document/E-ON/E-ON-2-aid-connect.JPG)

### 5. Troubleshooting
  You can monitor Azure IoT Edge / EdgeHub log by below command:
  ```
  docker logs edgeHub -f
  ```
#### 5.1 TLS handshake failed
  "TLS handshake failed" means AIG-301 can't verify the X.509 certificate which sent from Azure IoT Edge / EdgeHub. It cloud be one or some below reasones:
  - The Subject CN value doesn't match GatewayHostName
  - The X.509 certificate expired
  - AIG-301 trusted Root CA fails on the X.509 certificae validataion
  - You import wrong trusted Root CA for AIG-301

#### 5.2 Unable to authenticate client xxx with cached service identity xxx (Found: False)
  xxx is the child device ID.
  
  This error means that the device ID (xxx) is not be assigned as child device of Azure IoT Edge. You shall review and apply correct configuration on Azure IoT Hub.
  

