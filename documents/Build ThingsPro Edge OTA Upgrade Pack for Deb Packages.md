# Build ThingsPro Edge OTA Upgrade Pack for Deb Packages

Document Version: 1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-02-10 | document created. |



### Purpose

ThingsPro Edge offers over the air (OTA) upgrade function allow you to upgrade software which running on Moxa device, including：

1. Security Patch (.deb file)
2. OS Patch (.deb file)
3. Bug Fix (.deb file)
4. Your program (.deb file)

This document guides you how to pack all of them as one OTA upgrade pack.

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

   | Name               | Type   | Description                                                  |
   | ------------------ | ------ | ------------------------------------------------------------ |
   | data               | folder |                                                              |
   | data/task1         | folder |                                                              |
   | data/task1/debs    | folder | Copy all to be installed/upgraded deb files to this folder   |
   | data/task1/install | file   | An executable file to install all deb files from current debs folder |
   | package.yaml       | file   | Default package definition file, you may need to modify it later |

   

### 1. Basic Pack Steps

I would like to pack 1 or many deb files to be one ThingsPro OTA upgrade pack, and named it as "myFirstPack" with version 1.0.0

1. Copy all your deb files to ./data/task1/debs

2. Edit ./package.yaml, change "name" to be "myFirstPack", and keep version 1.0.0 as below

   ```
   kind: package
   version: v1
   metadata:
     name: myFirstPack
     version: 1.0.0
     arch: armhf
   spec:
     location: to-be-filled-by-tool
     packages:
       - name: task1
         displayName: Install task1
         path: task1
         version: 1.1.0
       # - name: task2
       #   displayName: Install MPKG
       #   path: edge-web_*_armhf.mpkg
       #   version: to-be-filled-by-tool
   ```

3. Run below command to build OTA pack：

   ```
   $ docker run -it --rm -u ${UID} -v `pwd`:/data moxa2019/thingspro-upgrade-packer:2.2.1 pack
   ```

   Packer creates a folder, build, at current location, it including：

   | Name                                          | Type   | Description                                       |
   | --------------------------------------------- | ------ | ------------------------------------------------- |
   | build                                         | folder |                                                   |
   | build/armhf                                   | folder | indicate CPU architecture                         |
   | build/armhf/myFirstPack_1.0.0_armhf.yaml      | file   | YAML file of myFirstPack                          |
   | build/armhf/myFirstPack_1.0.0_armhf.deb.zsync | file   | Index file of myFirstPack_1.0.0_armhf.deb         |
   | build/armhf/myFirstPack_1.0.0_armhf.deb       | file   | myFirstPack installer & to be installed deb files |



The basic pack shall fulfill most of your cases. You now can deploy myFristPack_1.0.0 to your filed devices.

##### Related documents：

- Deploy ThingsPro Edge OTA upgrade pack from Cloud.



### 2. Advance Pack 

I would like to pack many deb files to be one ThingsPro OTA upgrade pack, named it as "mySecondPack" with version 2.0.0 , and deal with each deb package name and version at different tasks.

Let us use 3 deb package as example：

| Package Name  | Version | Task  |
| ------------- | ------- | ----- |
| myProgram     | 1.2.2   | task1 |
| sqlLite-patch | 2.5.4   | task2 |
| libssl-patch  | 5.4.8   | task3 |

1. Create task2 and task3, and copy all the stuff from task1

   ```
   $ cd data
   $ cp -r task1 task2
   $ cp -r task1 task3
   ```

2. Copy each deb file(s) to each task's debs folder

   ```
   $ cp myProgram.deb ./data/task1/debs
   $ cp sqlLite-patch.deb ./data/task2/debs
   $ cp libssl-patch.deb ./data/task3/debs
   ```

3. Edit ./package.yaml, change "name" to be "mySecondPack",  version 2.0.0, add task 2 and task 3 sections, as below

   ```
   kind: package
   version: v1
   metadata:
     name: mySecondPack
     version: 2.0.0
     arch: armhf
   spec:
     location: to-be-filled-by-tool
     packages:
       - name: myProgram
         displayName: Install myProgram
         path: task1
         version: 1.2.2
       - name: sqlLite-patch
         displayName: Install sqlLit security patch
         path: task2
         version: 2.5.4
       - name: libssl-patch
         displayName: Install libssl patch
         path: task3
         version: 5.4.8
   ```

4. Run below command to build OTA pack：

   ```
   $ docker run -it --rm -u ${UID} -v `pwd`:/data moxa2019/thingspro-upgrade-packer:2.2.1 pack
   ```

   Packer creates a folder, build, at current location, it including：

   | Name                                           | Type   | Description                                        |
   | ---------------------------------------------- | ------ | -------------------------------------------------- |
   | build                                          | folder |                                                    |
   | build/armhf                                    | folder | indicate CPU architecture                          |
   | build/armhf/mySecondPack_2.0.0_armhf.yaml      | file   | YAML file of mySecondPack                          |
   | build/armhf/mySecondPack_2.0.0_armhf.deb.zsync | file   | Index file of mySecondPack_2.0.0_armhf.deb         |
   | build/armhf/mySecondPack_2.0.0_armhf.deb       | file   | mySecondPack installer & to be installed deb files |

   

##### Related documents：

- Deploy ThingsPro Edge OTA upgrade pack from Cloud.

