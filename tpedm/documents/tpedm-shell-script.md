# Download and Run Installation Script

##### 1. Please make sure Docker engine installed before install TPEDM.

```
sudo su
wget https://thingspro.blob.core.windows.net/tpe2/Python3/tpedm-install.sh
chmod 755 tpedm-install.sh
./tpedm-install.sh
```



##### 2. The TPEDM installation script create below folders.

| Folder                 | Desc                                                         |
| ---------------------- | ------------------------------------------------------------ |
| /home/tpedm/emqx       | EMQX MQTT Broker and plug-in configuration which requires by TPEDM |
| /home/tpedm/postgresql | Postgresql data files and configuration                      |
| /home/tpedm/web        | TPEDM Web Application source code and configuration          |



##### 3. The TPEDM installation script create below 3 docker containers.

| Container Instance | Docker Image    | Port host:container | Docker network |
| ------------------ | --------------- | ------------------- | -------------- |
| dm_database        | postgres:14.0   | 5432:5432           | dm_network     |
| dm_web             | dm_web:latest   | 80:80               | dm_network     |
| dm_emqx            | emqx/emqx:4.4.1 | 1883:1883           | dm_network     |



##### 4. Open Linux virtual machine firewall port (1883 and 80) to allow ThingsPro Edge devices and browser connection.



##### 5. Open browser, connect to Linux virtual machine IP with port 80

![](https://thingspro.blob.core.windows.net/resource/document/tpe/tpedm-devices.jpg)



# Operation Tips...

**Start / Stop EMQX**

```
docker start/stop dm_emqx
```



**Start/Stop Database**

```
docker start/stop dm_database
```



**Start/Stop Web App**

```
docker start/stop dm_web
```

<a href="https://github.com/abadar05/AIG301-501-Technical-Document/blob/main/documents/TPEDM-guide.md#for-developers">
For Developers Guideline... </a>

