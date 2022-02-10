# Build ThingsPro Edge OTA Upgrade Pack for MPKG Application

Document Version: 1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-02-10 | document created. |



### Purpose

ThingsPro Edge offers over the air (OTA) upgrade function allow you to install and/or upgrade ThingsPro Edge managed application (.mpkg format), particular build by yourself. This document guides you how to pack .mpkg appliation as OTA upgrade pack.

##### Related documents：

- Deploy ThingsPro Edge OTA upgrade pack from Cloud.
- Setup X.509 mutual authentication OTA upgrade process on ThingsPro Edge.



### Environment Preparation

1. A X86 PC or VM with Ubuntu 18.04+

2. Install Docker engine

3. Install ThingsPro Edge Upgrade Packer docker image

   ```
   $ docker pull moxa2019/thingspro-upgrade-packer:2.2.1
   ```

4. Run below commands to create a working folder, packer, and necessary files

   ```
   $ mkdir packer
   $ cd packer
   $ docker run -it --rm -u ${UID} -v `pwd`:/data moxa2019/thingspro-upgrade-packer:2.2.1 create
   ```


5. Below are files be created

   | Name         | Type   | Description                                                  |
   | ------------ | ------ | ------------------------------------------------------------ |
   | data         | folder |                                                              |
   | data/task1   | folder | this folder is nothing related with .mpkg application. Ignore it. |
   | package.yaml | file   | Default package definition file, you may need to modify it later |
   
   

### 1. MPKG Pack Steps

I would like to pack Azure IoT Central Demo app version 1.2.0 to be ThingsPro OTA upgrade pack, and named it as "AIC-Demo" with version 1.2.0

1. Download and copy Azure IoT Central Demo mpkg to ./data

   ```
   $ wget https://thingspro.blob.core.windows.net/software/edge/others/aic_1.2-650_armhf.mpkg
   $ cp aic_1.2-650_armhf.mpkg ./data
   ```

2. Edit ./package.yaml, change "name" to be "AIC-Demo", version 1.2.0, and assign mpkg file name to patch field, as below

```
kind: package
version: v1
metadata:
  name: AIC-Demo
  version: 1.2.0
  arch: armhf
spec:
  location: to-be-filled-by-tool
  packages:
    - name: AIC-Demo
      displayName: Install Azure IoT Central Demo App
      path: aic_1.2-650_armhf.mpkg
      version: 1.2.0
```

3. Run below command to build OTA pack：

```
$ docker run -it --rm -u ${UID} -v `pwd`:/data moxa2019/thingspro-upgrade-packer:2.2.1 pack
```

Packer creates a folder, build, at current location, it including：

| Name                                       | Type   | Description                            |
| ------------------------------------------ | ------ | -------------------------------------- |
| build                                      | folder |                                        |
| build/armhf                                | folder | indicate CPU architecture              |
| build/armhf/AIC-Demo_1.2.0_armhf.yaml      | file   | YAML file of AIC-Demo_1.2.0            |
| build/armhf/AIC-Demo_1.2.0_armhf.deb.zsync | file   | Index file of AIC-Demo_1.2.0_armhf.deb |
| build/armhf/AIC-Demo_1.2.0_armhf.deb       | file   | AIC-Demo_1.2.0 installer               |



##### Related documents：

- Deploy ThingsPro Edge OTA upgrade pack from Cloud.

