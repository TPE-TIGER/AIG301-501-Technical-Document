# Install/Upgrade ThingsPro Edge Application from Cloud (OTA Software Upgrade)

Document Version: 1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2023-03-02 | document created. |

### Purpose

This article explains how to install and/or upgrade ThingsPro Edge application from cloud, such as via Azure IoT Hub and AWS IoT Core. This is very common and important operational task in IIoT project, as named OTA software upgrade. 



##### Related documents：

- <a href="https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/Build%20ThingsPro%20Edge%20OTA%20Upgrade%20Pack%20for%20Deb%20Packages.md">Build ThingsPro Edge OTA Upgrade Pack for Debian Packages.</a>

- <a href="https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/Build%20ThingsPro%20Edge%20OTA%20Upgrade%20Pack%20for%20MPKG%20application.md">Build ThingsPro Edge OTA Upgrade Pack for MPKG Application.</a>

  

### Azure IoT Hub

We are going to invoke an Azure IoT Hub Direct Method to launch OTA software upgrade from cloud to IIoT Gateway, such as AIG-301.

#### 1. Upload your software package files to Azure Blob storage

The package files included below 3 files, and please let all of them are public accessible.

| File      | Example                       | Note          |
| --------- | ----------------------------- | ------------- |
| xxx.yaml  | My-App2_1.0.0_armhf.yaml      | Public Access |
| xxx.zsync | My-App2_1.0.0_armhf.deb.zsync | Public Access |
| xxx.deb   | My-App2_1.0.0_armhf.deb       | Public Access |



#### 2. Connect your IIoT Gateway, such as AIG-301, to Azure IoT Hub

Of cause, you need to connect your IIoT Gateway to Azure IoT Hub either by Azure IoT Device or Azure IoT Edge.

If your IIoT Gateway connects as Azure IoT Edge, you have to deploy **thingspro-agent**, a module of Azure IoT Edge, before go for next.

About <a href="https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/thingspro-agent%20Release%20&%20Configuration.md">thingspro-agent release and configuration</a>.



#### 3. Invoke an Azure IoT Hub Direct Method

3.1 Login to Azure IoT Hub portal, find your **Device** or **Edge**.

3.2 On Device/Edge page, click **Direct method**, by fill with following data to invoke software upgrade

| Field              | Value                                                        |
| ------------------ | ------------------------------------------------------------ |
| Method name        | thingspro-software-upgrade                                   |
| Payload            | {<br/>    "downloadURL": "https://xxxx/xxx.yaml",<br/>    "runInstallation": true<br/>} |
| Response timeout   | Default shall be OK                                          |
| Connection timeout | Default shall be OK                                          |

![](https://thingspro.blob.core.windows.net/resource/document/tpe/Azure-OTA.JPG)

* downloadURL for testing: https://thingspro.blob.core.windows.net/software/edge/others/My-App2_1.0.0_armhf.yaml

3.3 Click **Invoke method** button, and you shall get result below

![](https://thingspro.blob.core.windows.net/resource/document/tpe/Azure-OTA-02.JPG)



------

### AWS IoT Core

We are going to submit an AWS IoT Core Job to launch OTA software upgrade from cloud to IIoT Gateway, such as AIG-301.

#### 1. Upload your software package files to AWS S3 storage

The package files included below 3 files, and please let all of them are public accessible.

| File      | Example                   | Note          |
| --------- | ------------------------- | ------------- |
| xxx.yaml  | My-App2_1.0.0_armhf.yaml  | Public Access |
| xxx.zsync | My-App2_1.0.0_armhf.zsync | Public Access |
| xxx.deb   | My-App2_1.0.0_armhf.deb   | Public Access |



#### 2. Upload AWS IoT Core Job definition file to AWS S3 storage

You need to provide Job definition file to AWS IoT Core when you submit a Job.

```
{
  "name": "thingspro-software-upgrade",
  "payload": "{\"downloadURL\":\"https://xxxx/xxx.yaml\",\"runInstallation\":true}"
}
```

Save it as file, and upload to AWS S3 storage. This file can be private.

- downloadURL for testing: https://thingspro.blob.core.windows.net/software/edge/others/My-App2_1.0.0_armhf.yaml



#### 3. Connect your IIoT Gateway, such as AIG-301, to AWS IoT Core

Of cause, you need to connect your IIoT Gateway to AWS IoT Core.



#### 4. Submit an AWS IoT Core Job

4.1 Login to AWS IoT Core console, from left-hand menu, select **Manage / Remote actions / Jobs**

4.2 Click **Create job** button, following screen and fill by below data:

| Item         | Value                                                        |
| ------------ | ------------------------------------------------------------ |
| Job type     | Create custom job                                            |
| Name         | Install-thingspro-edge-software                              |
| Job targets  | Things to run this job: **[Select one or many things you would like to deploy]** |
| Job document | From file: **[Browse S3, and pick up Job definition file you upload]** |
| Job run type | Snapshot                                                     |

4.3 Click **Submit** button, and you shall get result below

![](https://thingspro.blob.core.windows.net/resource/document/tpe/AWS-Job-01.JPG)

You can click **Refresh** button to get up to date status.