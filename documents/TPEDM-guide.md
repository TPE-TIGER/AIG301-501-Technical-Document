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

ThingsPro Device Management (TPEDM) requires a Linux virtual machine with Docker engine. TPEDM doesn't limit on any Linux distribution nor Docker engine version, however, installation script is base on Debian's packages and commands, we suggest go for below configuration that verified already.

| Linux                     | Docker Engine                          | Python3 (host) |
| ------------------------- | -------------------------------------- | -------------- |
| Ubuntu Server 21.10  | 20.10.14, build a224086 or up to dated | 3.9+           |
| Ubuntu Server 20.04  | 20.10.14, build a224086 or up to dated | 3.8+           |
| Debian 11.3.0             | 20.10.14, build a224086 or up to dated | 3.9+           |


# Download and Install TPEDM

1. <a href="https://github.com/abadar05/AIG301-501-Technical-Document/blob/main/tpedm/documents/tpedm-shell-script.md"> Install via shell script </a>
2. <a href="https://github.com/abadar05/AIG301-501-Technical-Document/blob/main/tpedm/documents/tpedm-docker-compose.md"> Install via docker compose </a>

The following new security features are included in docker-compose installation method:
1. Placed Nginx reverse proxy server in front of dm-web container
2. Enabled HTTPS (TLS/SSL) on Nginx, to protect communication between browser and web server.
3. Removed 5432 port on host which associate with dm_database. Now database initialization python script converted into docker container associate with dm_database_init container communicates directly with dm_database by docker internal network adapter (dm_network). Therefore, no need to map database container port on host network. 


<h1 id="For Developers...">For Developers...</h1>

##### License

1. ThingsPro Device Management (TPEDM) is based on MIT license.
2. TPEDM leverages EMQX Community MQTT Broker. License：https://github.com/emqx/emqx/blob/master/LICENSE
3. TPEDM leverages Postgresql database. License：https://www.postgresql.org/about/licence/



##### Reference Architecture

![](https://thingspro.blob.core.windows.net/resource/document/tpe/tpedm-ra.jpg)

1. TPEDM could be deploy at on-premise or off-premise. The key point is field devices (TPE device on diagram) are able to connect to TPEDM on MQTT port (1883 on diagram).
2. There are 3 Docker containers running on a virtual machine, and able to communicate each other via Docker network adapter internally.
3. Line 1 (from EMQX webhook to Web restful API). Configure EMQX webhook to invoke Web's Restful API when below event happen:
   - device connected with EMQX. Web Restful API then update device connection status back to database and to user browser.
   - device disconnect from EMQX. Web Restful API then update device connection status back to database and to user browser.
   - device send Restful API execution response to MQTT topic：/tpe/{Client ID}/output. Web Restful API then forward the result to user browser.
4. Line 2 (from Web restful API to EMQX restful API). 
   - Web application retrieves device MQTT connection data from EMQX, and present to user browser.
   - Web application submit a device management command to MQTT broker, which apply by user on browser.
5. Line 3 (from Web restful API to Database). These are simple CRUD operation for device entity on database.
6. Line 4 (from EMQX to Database). Configure EMQX to connect to database for query and authenticate device. 



##### EMQX Plug-In

1. Auth_Postgresql：EMQX be enabled auth_postgresql plug-in to authenticate remote device identity. There are two files related with this plug-in.
   - **/home/tpedm/emqx/loaded_plugins**. This file enables EMQX to load auth_pgsql plugin.
   - **/home/tpedm/emqx/etc/plugins/emqx_auth_pgsql.conf**. This file define postgresql database and requires sql statement.
2. Web_hook：EMQX be enabled Web_hook plug-in to route below events happen on each devices to dm_web Restful API.
   - **/home/tpedm/emqx/loaded_plugins**. This file enables EMQX to load web_hook plugin.
   - **/home/tpedm/emqx/etc/plugins/emqx_web_hook.conf**. This file define where is web URL and listening events.



##### Postgresql 

1. During TPEDM installation, /home/tpedm/web/initDatabase.py program is in charge to create database, tables, and data. You may want to modify this program to co-operate with your add-on tables.

2. Database name：tpedm

   The database name, **tpedm**, been specify on dm_emqx and dm_web. Be careful if you want to change the name.

3. Tables：

   - TABLE / mqtt_user：this table stores device's identity and credential. EMQX query and authenticate device by these data.

   - TABLE / clientid_profile：this table stores device's profile, connection status and last update time.

   - TABLE / dm_category：this table stores device management operation category, for user to select associate management   command easy.

   - TABLE / dm_operation：this table stores ThingsPro Edge Restful APIs which allow be invoked through MQTT broker. The data source be defined at /home/tpedm/web/data/command.json.  However, due to resource constraint, not all available operation command be check-in to TPEDM at day 1. You can import all others by yourself, or let us know what else are important to your business.

     ThingsPro Edge Restful API：https://thingspro-edge.moxa.online/ 



##### Web Application

1. Web Application is only one place to extent and customize your device management application by programming code, Python 3.

2. The source code located at **/home/tpedm/web**, and will be mount into dm_web container. You can just update the source code and restart dm_web container directly.

3. The file **/home/tpedm/web/data/config.json** defines all necessary and important setting which requires by web application.

   - web section. The IP and port be used by web application container.
   - database section. Postgresql database connection inforamtion.
   - EMQX restful API. The URL and credential to invoke EMQX restful API.
   - ThingsPro Cloud API. The URL and credential to invoke ThingsPro Cloud software repo.

   

##### Device Connection Status

1. For better system performance, Web Application retrieves device profile and connection status from database directly. This assumes all associated components (EMQX webhook, Web Application and database) all functions well and expected. However, this assumption may not true, you shall consider to implement a schedule job at back end to synchronized in-consistent data. 



##### Device Management Category and Operation

1. <a href="https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/Invoke%20ThingsPro%20Edge%20Restful%20API%20from%20MQTT%20Server.md">This document</a> describes what is "Invoke Restful API from MQTT broker", and what are payload for input and output.

2. Due to technical barrier and dangerous behavior, below types of restful API are not in support list：

   - Non application/json content type. For example, file import/export.

   - /auth

   - /device/route

     

##### Scalability and Performance

​	You shall consider to deploy a scalabile and high performance production environment.

1. Clustering MQTT Broker (https://www.emqx.io/docs/en/v4.3/advanced/cluster.html#distributed-erlang) is good idea to handle mass concurrent devices and come with high availability features.
2. Separate Web Application web hook API from current dm_web container, and deploy it on a dedicate VM node.
3. Introduce Kubernestes application framework, distribute and deploy TPEDM containers on it.



##### Security

​	You shall consider to apply below policy and mechanism to protect your production environment.

1. Web server proxy. Place a web server proxy, such as Nginx, at frond of dm_web container is highly recommend.
   - https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04
2. Enable HTTPS (TLS/SSL) on Nginx, to protect communication between browser and web server.
   - http://nginx.org/en/docs/http/configuring_https_servers.html
3. Enable TLS/SSL on EMQX, to protect communication between devices and MQTT broker.
   - https://www.emqx.com/en/blog/emqx-server-ssl-tls-secure-connection-configuration-guide
4. You can remove 5432 port on host which associate with dm_database. The port (5432) created on host is for first time database table and data initialization only. Afterward, both dm_web and dm_emqx connect to dm_database by docker internal network adapter (dm_network).
5. User account. You shall implement user authentication and authorization function on top of TPEDM, no doubt.

