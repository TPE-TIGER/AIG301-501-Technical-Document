# AIG Software Release & Upgrade

Document Version: 1.1

### Change Log

| Version | Date       | Content                         |
| ------- | ---------- | ------------------------------- |
| 1.0     | 2022-08-05 | Content Created                 |
| 1.1     | 2022-09-22 | Add AIG-301 V1.4 & AIG-501 V1.2 |
| 1.2     | 2023-08-31 | Add AIG-301 V1.5                |



# AIG-300 Series

### 

Important notice: Please read the release note and upgrade note, and make sure to execute local test before deploying the upgrade to the remote units.

### Upgrade to AIG-301 version 1.5

**Pre-request：AIG-301 version 1.4**

|      | Description                                 | OTA URL                                                      |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | Upgrade pack for AIG-301 (IMG 1.4 to 1.5) | https://files.thingsprocloud.com/package/Upgrade_AIG-301_2.4.0-4020_IMG_1.4_to_1.5.deb.yaml |

- Release note: https://files.thingsprocloud.com/package/AIG_301_v1.5_ReleaseNotes_final.pdf
- Upgrade note: https://files.thingsprocloud.com/package/AIG_301_v1.5_UpgradeNotes_final.pdf

### Upgrade to AIG-301 version 1.4

**Pre-request：AIG-301 version 1.3**

|      | Description                                 | OTA URL                                                      |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | Upgrade pack for AIG-301 (IMG 1.3 to 1.4) | https://files.thingsprocloud.com/package/Upgrade_AIG-301_2.3.1-3657_IMG_1.3_to_1.4.deb.yaml |


### Upgrade to AIG-301 version 1.3

**Pre-request：AIG-301 version 1.2**

|      | Description                                 | OTA URL                                                      |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | Upgrade pack 1 for AIG-301 (IMG 1.2 to 1.3) | https://files.thingsprocloud.com/package/Upgrade_AIG-301_Rev_2.0.0_IMG_1.2_to_1.3.yaml |
| 2    | Upgrade pack 2 for AIG-301 (IMG 1.2 to 1.3) | https://files.thingsprocloud.com/package/package_2.2.1-3369-aig_armhf.yaml |



### Upgrade to AIG-301 version 1.2

**Pre-request：AIG-301 version 1.1**

|      | Description                               | OTA URL                                                      |
| ---- | ----------------------------------------- | ------------------------------------------------------------ |
| 1    | Upgrade pack for AIG-301 (IMG 1.1 to 1.2) | https://files.thingsprocloud.com/package/platform_2.2.0_armhf.yaml |



# AIG-500 Series

### Upgrade to AIG-501 version 1.2

**Pre-request：AIG-501 version 1.1**

|      | Description                                 | OTA URL                                                      |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | Upgrade pack for AIG-501 (IMG 1.1 to 1.2) | https://files.thingsprocloud.com/package/Upgrade_AIG-501_2.3.1-3658_IMG_1.1_to_1.2.deb.yaml |


### Upgrade to AIG-501 version 1.1

**Pre-request：AIG-501 version 1.0**

|      | Description                                 | OTA URL                                                      |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | Upgrade pack 1 for AIG-501 (IMG 1.0 to 1.1) | https://files.thingsprocloud.com/package/Upgrade_AIG-501_Rev_1.0.0_IMG_1.0_to_1.1.yaml |
| 2    | Upgrade pack 2 for AIG-501 (IMG 1.0 to 1.1) | https://files.thingsprocloud.com/package/package_2.2.1-3369-aig_amd64.yaml |



------



### 1. How to find versions information on my device?

On ThingPro Edge Admin Web, click System Overview page to catch **Firmware Ver.** and **ThingsPro Ver.** 

![](https://docs.moxa.online/assets/images/Overview_2-b2178d4fd6a59c227b49812cbbb00f18.png)



### 2. Verify Software Upgrade Dependency

Before upgrade software, you shall verify the dependency according to this document, and following the upgrade path (1.1 to 1.2, 1.2 to 1.3 and so on)



### 3. Software Upgrade

There are couple methods to submit software upgrade command.

##### Option 1：By ThingsPro Edge Admin Web (/General Operation/ Software Upgrade)

##### Option 2：By ThingsPro Edge Restful API, https://docs.moxa.online/tpe/openapi/core#tag/upgrade

​	Step 1: Create upgrade job, https://docs.moxa.online/tpe/openapi/core#tag/upgrade/paths/~1upgrades/post

​	Step 2: Start the job, https://docs.moxa.online/tpe/openapi/core#tag/upgrade/paths/~1upgrades~1%7Bid%7D~1%7Baction%7D/put

##### Option 3：By Azure IoT Hub Direct Method Command or AWS IoT Core Job
Refer to <a href="https://github.com/TPE-TIGER/AIG301-501-Technical-Document/blob/main/documents/Install-Upgrade%20ThingsPro%20Edge%20Application%20from%20Cloud.md">Install/Upgrade ThingsPro Edge Application from Cloud</a>.



------



