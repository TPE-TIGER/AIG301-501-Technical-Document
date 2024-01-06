# Getting started 
## Step1: Clone GitHub Repository
 ```
sudo apt-get update && sudo apt-get install git \
&& sudo git clone https://github.com/abadar05/AIG301-501-Technical-Document.git \
&& cd AIG301-501-Technical-Document/tpedm/ \
&& sudo mkdir -p certs/ssl/
 ```
 ```
sudo mkdir -p certs/ssl/
 ```
## Step 2: Generate SSL Certificate and Private Key
Generate a Self-Signed SSL Certificate and Private Key using OpenSSL.
Run the following command to generate a self-signed SSL certificate and key under /certs/ssl/ directory

 ```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./certs/ssl/privatekey.key -out ./certs/ssl/certificate.crt
 ```

## Step3: Install TPEDM Application using Docker Compose
#### 1. Please make sure Docker engine and docker-compose installed before install TPEDM.

set UID and GID in the shell before running docker-compose up. This approach ensures that the containers runs with the same user permissions as the host user, mitigating permission-related issues when accessing the mounted volume.

```
sudo su
export UID=$(id -u)
export GID=$(id -g)
```
```
sudo docker-compose up -d
```


##### 2. The TPEDM directory includes below folders and files

| Folder                      | Desc                                                                   |
| --------------------------- | ---------------------------------------------------------------------- |
| /tpedm/emqx                 | EMQX MQTT Broker and plug-in configuration which requires by TPEDM     |
| /tpedm/web                  | TPEDM Web Application source code and configuration                    |
| /tpedm/postgresql-init      | Database initialization source code data files and configuration        | 
| /tpedm/postgresql           | Postgresql directory created by docker-compose, mount container volume |                                         
| /tpedm/certs/ssl            | Nginx self signed server certificate and private key                   |
| /tpedm/documents            | Readme files for TPEDM                                                 |
| /tpedm/docker-compose.yml   | Docker compose file to launch TPEDM                                    |
| /tpedm/nginx.conf           | Nginx server configuration file                                        |




##### 3. The TPEDM Docker Compose file create below 5 docker containers.

| Container Instance | Docker Image           | Port host:container | Docker network |
| ------------------ | ---------------------- | ------------------- | -------------- |
| dm_database        | postgres:14.0          | 5432(container only)| dm_network     |
| dm_web             | dm_web:latest          | 80:80               | dm_network     |
| dm_emqx            | emqx/emqx:4.4.1        | 1883:1883           | dm_network     |
| dm_nginx           | nginx:latest           | 443:443             | dm_network     |
| dm_database-init   |dm_database_init:latest |  N/A                | dm_network     |



##### 4. Open Linux virtual machine firewall port (1883 and 443) to allow ThingsPro Edge devices and browser connection.



##### 5. Open browser, connect to Linux virtual machine IP with port 443

![](https://thingspro.blob.core.windows.net/resource/document/tpe/tpedm-devices.jpg)



# Operation Tips...

**Start/Stop Entire TPEDM Application**

```
docker-compose down
docker-compose up
```

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
