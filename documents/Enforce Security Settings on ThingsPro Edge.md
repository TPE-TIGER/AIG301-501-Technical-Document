# Enforce Secured Setting on ThingsPro Edge

Document Version: V1.1

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.1     | 2022-03-02 | document created. |

### Purpose

This document lists out the recommended actions to be taken in ThingsPro Edge before deployments, to secure IIoT gateways in the field.

---

### 1. Manage Roles and Users

The user should be aware that information containing the default account and password is publically available to everyone, and thus it should only be used for the purpose of installation.

#### 1.1 Create New Roles and Users

It's recommended to create new user accounts for each individual with adequate permissions. In ThingsPro Edge, permissions can be grouped as roles, then further assigned to user accounts. 

#### 1.2 Disable or Change the Password for Default Account

Once user accounts have been created, user should either remove the default account, or change the default password of it. 

> Note: To avoid from being unintentionallty locked out from the gateway, ThingsPro Edge does not allow the last user account assigned administrator role to be removed.


### 2. Disable Unused Interfaces

The user should disable unused interfaces to prevent unexpected access to the gateway.

> Note: The user must realize that although the gateway has become more secured by disabling unused interfaces, the tradeoff is it's resilience because the backup options to access the gateway have been disabled.
<p align="center" width="100%"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/serviceEnable.JPG" width="600" /></p>

#### 2.1 Network

Validate the network interface settings and disable the unused ones.

- Cellular
- DHCP Server
- LAN
- Wi-Fi

#### 2.2 Service

##### 2.2.1 HTTP(S) Service

ThingsPro Edge enables HTTPS for gateway initialization by default. The user should disable it once the gateway has been properly configured to prevent unexpected access.

##### 2.2.2 Local Console

ThingsPro Edge leaves console port enabled by default for debug purpose. The user should disable it before deploying the gateway to an unattended location.

##### 2.2.3 NAT Service

ThingsPro Edge allow south-bound device connect to Internet directly via enable NAT Service. The user should disable it if no such requirement.

##### 2.2.4 SD Card

ThingsPro Edge disables SD card by default. The user should enable it only when required, and do not storing sensitive data on it to mitigate the risk of losing it.

##### 2.2.5 SSH Server

ThingsPro Edge disables SSH server by default. It's common that the user may enable it to gain further control for device initialization. However, it should be disabled once the gateway has been properly configured to prevent unexpected access.

#### 2.3 Provision Service

##### 2.3.1 ThingsPro Proxy

ThingsPro Edge support auto provisioning by ThingsPro Proxy, which requires ThingsPro Edge to open a port for device discovery. Please disable it after the device has been provisioned.



### 3. Configure the System

The user should have the security related settings properly setup to enhance gateway security.

#### 3.1 Time - Timezone and Date Time

System time is widely used in security related actions, such as certificate validation. The user should configure system time zone and time properly and enable auto sync if possible.

#### 3.2 HTTPS - Replace by your own X.509 certificate

If, for some reason, the user decides to leave https service enabled in the field, it's recommended to import your own certificate and private key for the HTTPS service, so user's working laptop can successfully validate the identity of the gateway.

The HTTPS service on ThingsPro Edge comes with a set of self-signed certificate and private key by default. If the user is not able to replace the default with your own certificate and private key, we recommend the user to export the default root certificate from ThingsPro Edge and add it to the trusted root certificate authority list on your working laptop.

#### 3.3 Firewall - Review the inbound policy

- Review the firewall inbound policy and ensure that only the necessary/recognized service/ports are listed in the inbound allowed list.

- ThingsPro Edge exposes only the 8443 port for HTTPS service by default.

  <p align="center" width="100%"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/Firewall.JPG" width="860" /></p>

#### 3.4 System Log - Storage Setting

The default storage size for keeping system logs is 100 Mb. The user should adjust the setting based on the application's need.

<p align="center" width="100%"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/systemlogsize.JPG" width="480" /></p>


### 4. X.509 Certificate based Mutual Authentication

All the cloud applications in ThingsPro Edge supports X.509 certificate based authentication, including:

- Azure IoT Edge
- Azure IoT Device
- AWS IoT Core
- MQTT Client
- Sparkplug

Please always consider using X.509 certificate based authentication in production.

<p align="center" width="100%"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/x509.JPG" width="480" /></p>
