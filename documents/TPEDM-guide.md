# What is TPEDM?

##### 1. ThingsPro Edge Device Management.

TPEDM is reference architecture for customer self-host device management application, which contains

- Installation Script
- Source Code
- For Developers' Notes

##### 2. TPEDM is open source by MIT license

##### 3. TPEDM contributes by ThingsPro Edge community and available on GitHub (https://github.com/tpe-tiger)

##### 4. Functionalities of TPEDM：

- Register a new device (which running with ThingsPro Edge software)
- Scan available software update from ThingsPro Cloud for each devices
- Present devices connection status in real-time and live
- Present devices basic profile
- Allow device administrator to invoke almost all ThingsPro Edge Restful API on TPEDM for device management, application configuration and software update



# Linux and Docker Engine

ThingsPro Device Management (TPEDM) requires a Linux virtual machine with Docker engine. Although TPEDM doesn't limit on any Linux distribution nor Docker engine version, but we suggest go for below configuration that we verified already.

**Linux**：Ubuntu Focal 20.04 (LTS)

**Docker engine**：Docker version 20.10.14, build a224086



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



# For Developers...

##### License

1. ThingsPro Device Management (TPEDM) is based on MIT license.
2. TPEDM leverages EMQX Community MQTT Broker. License：https://github.com/emqx/emqx/blob/master/LICENSE
3. TPEDM leverages Postgresql database. License：https://www.postgresql.org/about/licence/



##### Security

​	You shall consider to apply below policy and configuration to protect your production environment.

1. Web server proxy. Place a web server proxy, such as Nginx, at frond of dm_web container is highly recommend.
2. Enable HTTPS (TLS/SSL) on Nginx, to protect communication between browser and web server.
3. Enable TLS/SSL on EMQX, to protect communication between devices and MQTT broker.
4. You can remove 5432 port on host which associate with dm_database. The port (5432) created on host is for first time database table and data initialization only. Afterward, both dm_web and dm_emqx connect to dm_database by docker internal network adapter (dm_network).
5.  User account. You shall implement user authentication and authorization function on top of TPEDM, no doubt.



##### EMQX Plug-In

1. Auth_Postgresql：EMQX be enabled auth_postgresql plug-in to authenticate remote device identity. There are two files related with this plug-in.
   - ddd
   - ddd
2. Web_hook：EMQX be enabled Web_hook plug-in to route below events happen on each devices to dm_web Restful API.
   - ddd
   - ddd
   - ddd



##### Postgresql 

1. During TPEDM installation, 
2. database name
3. tables



##### Device Management Category and Operation
