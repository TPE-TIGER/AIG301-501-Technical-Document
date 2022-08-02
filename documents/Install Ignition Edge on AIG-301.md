# Install Ignition Edge on AIG-301

Document Version: V1.1

### Change Log

| Version | Date       | Content                   |
| ------- | ---------- | ------------------------- |
| 1.1     | 2022-08-02 | use Ignition edge edition |

### Purpose

This document states how to install Ignition Edge as an Azure IoT Edge ***Module*** on AIG-301.

---

### 1. Reset AIG-301 to Factory Default

Ignition Edge consumes a lot of resource (memory、storage and CPU), which may result in out of memory issue, particularly, if there were others heavy programs running on AIG-301 already, please stop or un-install them before you go.

The most easy way is to reset AIG-301 to factory default by below command:

```
sudo mx-system-mgmt -d restore
```



### 2. Provision AIG-301 to Azure IoT Hub as an IoT Edge

Follows by ThingsPro Edge user manual (https://thingspro-edge.moxa.online/v2.3.0/user-manuals/index.html), apply appropriate configuration and provision AIG-301 as Azure IoT Edge to Azure IoT Hub.



Install ***thingspro-agent module*** on Azure IoT Edge. This is optional for Ignition Edge, but if you need device management capability from Azure IoT Hub, it is what you need. Please refer to thingspro-agent version rlease document (https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/thingspro-agent%20Release%20&%20Configuration.md).



You shall able to see result like below screen shot. There are 3 modules running, and Azure IoT Edge running as well. It is fine the versions may be different according to ThingsPro Edge version and how to configuration on Azure IoT Hub.

![](https://thingspro.blob.core.windows.net/resource/document/tpe/AIE-UI.jpg)



### 3. Install Ignition Edge Module on Azure IoT Edge

Inductive Automation released Ignition Edge module on marketplace, which you can install and deploy it from Azure Cloud to your IIoT Gateway easier.

Access to Ignition Edge marketplace: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/inductiveautomation1644533469785.iot_edge_ignition_iiot1_byol?tab=Overview

<img src="https://thingspro.blob.core.windows.net/resource/document/tpe/ignition-marketplace.jpg" style="zoom:80%;" />

Click ***"Get It Now"***, and following each steps to install Ignition Edge module on the IIoT Gateway you desired.



#### Change Edition from *standard* to *edge*

By update Module Environment Variables, you can change Ignition edition to ***edge***

![](https://thingspro.blob.core.windows.net/resource/document/tpe/ignition-module-edition-edge.jpg)



#### Problem 1: Incorrect module name

You may encounter module name incorrectly issue like below screen.

![](https://thingspro.blob.core.windows.net/resource/document/tpe/ignition-module-name-fail.jpg)

Please move to Module configuration user interface, and rename it with appropriate name.

<img src="https://thingspro.blob.core.windows.net/resource/document/tpe/ignition-module-name-ok.jpg" style="zoom:80%;" />



#### Problem 2: Container Privileged

AIG-301 (arm32 CPU + Debian 9 OS) come with libseccomp2 (2.3.1), which had known issue to deal with "clock_gettime"...; refer to:

- https://github.com/dotnet/dotnet-docker/issues/3253
- https://github.com/dotnet/dotnet-docker/issues/3253#issuecomment-956378676

To solve this issue, please add ***Privileged*** on container creation option. (Don't remove anything already existed.)

```
{
    "HostConfig": {
        "Privileged": true
    }
}
```



### 4. Launch Ignition Edge

Depend on network throughput, it take at least 30 min for download and deploy Ignition Edge docker image (1.85GB) on your IIoT Gateway.

![](https://thingspro.blob.core.windows.net/resource/document/tpe/ignition-module-ok.jpg)

After Ignition Edge is running, launch Ignition Edge admin web: http://{ip}:8088

<img src="https://thingspro.blob.core.windows.net/resource/document/tpe/ignition-module-web.jpg" style="zoom:67%;" />



### Test & Verified 

Above installation and deployment steps be tested and verified on:

| Model   | Version | ThingsPro Edge Version | CPU   |
| ------- | ------- | ---------------------- | ----- |
| AIG-301 | 1.3     | 2.2.1                  | arm32 |
| AIG-301 | 1.2     | 2.2.0                  | arm32 |
| AIG-501 | 1.0     | 2.2.0                  | x64   |

