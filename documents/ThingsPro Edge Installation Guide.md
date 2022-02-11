# ThingsPro Edge Installation Guide

Document Version: V1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-02-10 | document created. |



### Purpose

This document provides ThingsPro Edge software installation steps to those eligible models for post-install.

For those ThingsPro Edge pre-build models, such as AIG-301、AIG-501 and custom firmware, you can skip this document.

This document is not aim for upgrade ThingsPro Edge, please refer to related document below.

##### Related documents：

- [ThingsPro Edge Software Release & Download](https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/ThingsPro%20Edge%20Software%20Release.md)
- [Deploy ThingsPro Edge OTA upgrade pack from Cloud]()



### Step 1：Download and Install

According your device model, find out correct ThingsPro Edge **full download URL** from [ThingsPro Edge Software Release & Download](https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/ThingsPro%20Edge%20Software%20Release.md)

##### 1.1 Download and install ThingsPro Edge debian package

```
sudo wget {full download URL}
sudo dpkg -i ./{file name}
```

##### 1.2 Trace installation progress, and waiting for installation to the end. (This step may take 20~30 minutes)

```
journalctl -u update -f

Moxa update[1355]: level=info msg="device: 3/4 78%" origin=http
Moxa update[1355]: level=info msg="device: 3/4 81%" origin=http
Moxa update[1355]: level=info msg="device: 3/4 87%" origin=http
Moxa update[1355]: level=info msg="device: 4/4 0%" origin=http
Moxa update[1355]: level=info msg="device: 4/4 0%" origin=http
Moxa update[1355]: level=info msg="device: 4/4 0%" origin=http
Moxa update[1355]: level=info msg="device: 4/4 0%" origin=http
Moxa update[1355]: level=info msg="device: starting running" origin=http

Moxa update[1355]: level=info msg="stop appman" origin=http
Moxa update[1355]: level=info msg="stop update" origin=http
Moxa update[1355]: level=info msg="shutdown Server ..." origin=init
Moxa systemd[1]: Stopping MOXA ThingsPro Updater...
Moxa update[1355]: level=info msg="bye bye" origin=init
Moxa systemd[1]: Stopped MOXA ThingsPro Updater.
```

##### 1.3 Waiting ThingsPro Edge first time initialization

It take 5 minutes for ThingsPro Edge to initialize, please wait.

You can trace initialization status by command:

```
root@Moxa:/home/moxa# appman app ls
+--------------+--------------+-----------------------+--------+
|     NAME     |   VERSION    | STATE (DESIRED STATE) | HEALTH |
+--------------+--------------+-----------------------+--------+
| cloud        | 2.2.1-1499   | ready (ready)         | good   |
| device       | 2.2.1-3736   | ready (ready)         | good   |
| dlmclient    | 2.2.1-1485   | ready (ready)         | good   |
| edge-web     | 1.23.37-5380 | ready (ready)         | good   |
| function     | 1.0.0-166    | ready (ready)         | good   |
| modbusmaster | 1.4.0-659    | ready (ready)         | good   |
| opcuaserver  | 2.1.0-644    | ready (ready)         | good   |
| tagservice   | 2.2.1-601    | ready (ready)         | good   |
+--------------+--------------+-----------------------+--------+
```

All states change to ready and with health/good, which means initialization completed.



##### Important Note:

1. After ThingsPro Edge installed..
   - LAN1 be configurated by DHCP mode
   - LAN2 remains as static IP (192.168.4.127)
   - SSH be disabled by default

2. We recommend you login to device either by <span style='color:blue'>SSH via LAN2</span> or<span style='color:blue'> local console serial port</span> to run installation task.



### Step 2：Launch ThingsPro Edge Web Admin Console

##### 1. ThingsPro Edge Web Admin

ThingsPro Edge Web Admin is starting by default on all network interfaces with

- Port：8443 (HTTPS)
- Default User：admin
- Default Password：admin@123

##### 2. Access to Web Admin by LAN1

If you know what IP be assigned for LAN1, then, open browser on laptop/PC, and connect to ThingsPro Edge Web Admin: https://{LAN1 IP}:8443

if you don't know LAN1's IP address, go for next step.

##### 3. Access to Web Admin by LAN2

Connect your laptop/PC Ethernet cable direct to device's LAN2 with proper IP address, such as 192.168.4.10 (255.255.255.0)

Open browser on laptop/PC, and connect to ThingsPro Edge Web Admin: https://192.168.4.127:8443

##### 4. TLS/SSL Warning message

It is expect that browser shows below TLS/SSL warning message, due to ThingsPro Edge Web Admin present a untrusted X.509 certificate. There are some ways to solve this issue, but, please skip this warning and go ahead this moment.

<div style="text-align:center"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/SSL_Warning.JPG" width="480" /></div>



##### 5. Accepted End-User License Agreement

On login page, please **read end-user license agreement**, and input default userID and password afterward.

<div style="text-align:center"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/login.JPG" width="480" /></div>



##### 6. Welcome to IIoT world and enjoy ThingsPro Edge



<div style="text-align:center"><img src="https://thingspro.blob.core.windows.net/resource/document/tpe/after-login.JPG" width="480" /></div>







