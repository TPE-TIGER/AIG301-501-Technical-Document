# AIG Software Release & Upgrade

Document Version: 1.0

### Change Log

| Version | Date       | Content         |
| ------- | ---------- | --------------- |
| 1.0     | 2022-08-05 | Content Created |

------

### 1. How to find versions information on my device?

ThingsPro Edge system overview page displays **Firmware Ver.** and **ThingsPro Ver.** 

![](https://docs.moxa.online/assets/images/Overview_2-b2178d4fd6a59c227b49812cbbb00f18.png)



### 2. Verify Software Upgrade Dependency

Before submit software upgrade command to device, you shall verify the dependency according to this document.



### 3. Submit Software Upgrade

There are couple methods to submit software upgrade commands.

##### Option 1：By ThingsPro Edge Admin Web (/General Operation/ Software Upgrade)

##### Option 2：By ThingsPro Edge Restful API, https://docs.moxa.online/tpe/openapi/core#tag/upgrade

​	Step 1: Create upgrade job, https://docs.moxa.online/tpe/openapi/core#tag/upgrade/paths/~1upgrades/post

​	Step 2: Start the job, https://docs.moxa.online/tpe/openapi/core#tag/upgrade/paths/~1upgrades~1%7Bid%7D~1%7Baction%7D/put

##### Option 3：By Azure IoT Hub Direct Method Command, thingspro-software-upgrade, https://docs.moxa.online/tpe/users-manual/northbound/azure-iotedge/ta_command



------

### AIG-301 version 1.3

| Type | Description          | OTA Upgrade URL                                              | Dependency   |
| ---- | -------------------- | ------------------------------------------------------------ | ------------ |
| TPE  | Upgrade TPE to 2.2.1 | https://files.thingsprocloud.com/package/package_2.2.1-3369-aig_armhf.yaml | Firmware 1.3 |
|      |                      |                                                              |              |

### AIG-301 version 1.2

| Type | Description                         | OTA Upgrade URL                                              | Dependency   |
| ---- | ----------------------------------- | ------------------------------------------------------------ | ------------ |
| MIL  | Upgrade AIG-301 Firmware 1.2 to 1.3 | https://files.thingsprocloud.com/package/Upgrade_AIG-301_Rev_2.0.0_IMG_1.2_to_1.3.yaml | Firmware 1.2 |
|      |                                     |                                                              |              |

### AIG-301 version 1.1

| Type | Description                         | OTA Upgrade URL                                              | Dependency   |
| ---- | ----------------------------------- | ------------------------------------------------------------ | ------------ |
| MIL  | Upgrade AIG-301 Firmware 1.1 to 1.2 | https://files.thingsprocloud.com/package/platform_2.2.0_armhf.yaml | Firmware 1.1 |
|      |                                     |                                                              |              |



------

### AIG-501 version 1.1

| Type | Description          | OTA Upgrade URL                                              | Dependency   |
| ---- | -------------------- | ------------------------------------------------------------ | ------------ |
| MIL  | Upgrade TPE to 2.2.1 | https://files.thingsprocloud.com/package/package_2.2.1-3369-aig_amd64.yaml | Firmware 1.1 |
|      |                      |                                                              |              |



### AIG-501 version 1.0

| Type | Description                         | OTA Upgrade URL                                              | Dependency   |
| ---- | ----------------------------------- | ------------------------------------------------------------ | ------------ |
| MIL  | Upgrade AIG-501 Firmware 1.0 to 1.1 | https://files.thingsprocloud.com/package/Upgrade_AIG-501_Rev_1.0.0_IMG_1.0_to_1.1.yaml | Firmware 1.0 |
|      |                                     |                                                              |              |

