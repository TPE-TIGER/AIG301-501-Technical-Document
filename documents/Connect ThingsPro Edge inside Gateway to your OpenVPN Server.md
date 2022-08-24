# Connect "ThingsPro Edge inside" Gateway to your OpenVPN Server

Document Version: 1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-03-21 | document created. |



### Purpose

For ThingsPro Edge customers who would like to remote connect to IIoT Gateway via OpenVPN software, this document guides you how to download and setup OpenVPN client application which running on top of ThingsPro Edge.



### 1. Download and Install OpenVPN mpkg file

1. Login on your IIoT Gateway as su, and download openvpn client mpkg installation file.

   ```
   $ sudo su
   $ wget https://thingspro.blob.core.windows.net/software/edge/others/openvpn_1.0.1-36_armhf.mpkg
   ```

2. Install it by ThingsPro Edge appman command.

   ```
   root@Moxa:/home/moxa# appman app install openvpn_1.0.1-36_armhf.mpkg
   
   {
     "data": {
       "arch": "armhf",
       "attributes": null,
       "availableVersions": [],
       "category": "dlm",
       "cpu_percent": 0,
       "description": "MOXA OpenVPN service",
       "desiredState": "ready",
       "displayName": "openvpn",
       "hardwares": [],
       "health": "wait",
       "icon": "",
       "id": "openvpn",
       "imageSize": 57777664,
       "mem_limit": 0,
       "name": "openvpn",
       "ports": {
         "filter": null,
         "forward": null
       },
       "state": "init",
       "version": "1.0.1-36"
     }
   }
   ```

3. Verify openvpn client be installed well without issue.

   ```
   root@Moxa:/home/moxa# appman app ls
   +--------------+-------------+-----------------------+--------+
   |     NAME     |   VERSION   | STATE (DESIRED STATE) | HEALTH |
   +--------------+-------------+-----------------------+--------+
   | cloud        | 2.2.1-1587  | ready (ready)         | good   |
   | device       | 2.3.0-3818  | ready (ready)         | good   |
   | dlmclient    | 2.2.1-1588  | ready (ready)         | good   |
   | edge-web     | 1.35.0-5544 | ready (ready)         | good   |
   | function     | 1.0.0-241   | ready (ready)         | good   |
   | modbusmaster | 1.4.0-665   | ready (ready)         | good   |
   | openvpn      | 1.0.1-36    | ready (ready)         | good   | 
   | tagservice   | 2.2.1-607   | ready (ready)         | good   |
   +--------------+-------------+-----------------------+--------+
   ```



### 2. Restful API of OpenVPN Client on top of ThingsPro Edge

The OpenVPN client application contains below restful API：

| End Point               | Method | Content Type                        | Remark                                    |
| ----------------------- | ------ | ----------------------------------- | ----------------------------------------- |
| /api/v1/openvpn         | GET    | (response) application/json         | Get OpenVpn client setting                |
| /api/v1/openvpn         | PATCH  | (response) application/json         | Patch OpenVpn client setting              |
| /api/v1/openvpn/profile | POST   | (request) form-data                 | Import an OpenVpn client profile file     |
| /api/v1/openvpn/profile | GET    | (response) application/octet-stream | Export an OpenVpn client profile file     |
| /api/v1/openvpn/profile | DELETE | (response) application/json         | Delete Target OpenVpn client profile file |



##### 2.1 Get OpenVpn client setting

|                      | Value           | Remark                   |
| -------------------- | --------------- | ------------------------ |
| End Point            | /api/v1/openvpn |                          |
| Method               | GET             |                          |
| Header: mx-api-token | {API token}     | Restful API access token |

Request Example：

```
curl https://192.168.8.202:8443/api/v1/openvpn \
-X GET -H "Content-Type:application/json" \
-H "mx-api-token:$(cat /var/thingspro/data/mx-api-token)" -k
```

Response Example：

```
{
    "data": {
        "type": "openvpn",
        "enable": false,
        "status": false,
        "profile": "",
        "network": {
            "remoteIp": "",
            "localIp": "",
            "netmask": "",
            "gateway": ""
        }
    }
}
```

##### 2.2 Patch OpenVpn client setting

|                      | Value           | Remark                   |
| -------------------- | --------------- | ------------------------ |
| End Point            | /api/v1/openvpn |                          |
| Method               | PATCH           |                          |
| Header: mx-api-token | {API token}     | Restful API access token |

Request Example:

```
{
	"enable": true,
    "profile": "myclient.ovpn"   
}
```

Response Example:

```
{
    "type": "openvpn",
    "enable": true,
    "status": false,
    "profile": "myclient.ovpn",
    "network": {
        "remoteIp": "",
        "localIp": "",
        "netmask": "",
        "gateway": ""
    }
}
```

##### 2.3 Import an OpenVpn client profile file

|                      | Value                   | Remark                                                       |
| -------------------- | ----------------------- | ------------------------------------------------------------ |
| End Point            | /api/v1/openvpn/profile |                                                              |
| Method               | POST                    |                                                              |
| Header: mx-api-token | {API token}             | Restful API access t                                         |
| Form Data: filename  | {File Content}          | key must be 'filename'<br />value：openvpn content with file and extension by .ovpn |

Request Example:

![](https://thingspro.blob.core.windows.net/resource/document/vpn/openvpn-post-profile.jpg)

Response Example:

```
{
    "message": "Upload config successfully"
}
```

##### 2.4 Export an OpenVpn client profile file

|                      | Value                                          | Remark                                                       |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| End Point            | /api/v1/openvpn/profile?filename=myclient.ovpn | query string with field name : filename, and value contain full file name you upload. |
| Method               | GET                                            |                                                              |
| Header: mx-api-token | {API token}                                    | Restful API access token                                     |

Request Example:

```
curl https://192.168.8.202:8443/api/v1/openvpn/profile?filename=myclient.ovpn \
-X GET -H "Content-Type:application/json" \
-H "mx-api-token:$(cat /var/thingspro/data/mx-api-token)" -k
```

Response Example:

```
cipher AES-256-CBC

setenv FORWARD_COMPATIBLE 1
client
server-poll-timeout 4
nobind
remote 23.xx.xxx.xxx 1194 udp
remote 23.xx.xxx.xxx 443 tcp

dev tun
dev-type tun
ns-cert-type server
setenv opt tls-version-min 1.0 or-highest
reneg-sec 604800
sndbuf 0
rcvbuf 0
# NOTE: LZO commands are pushed by the Access Server at connect time.
# NOTE: The below line doesn't disable LZO.
comp-lzo no
verb 3
setenv PUSH_PEER_INFO

<ca>
-----BEGIN CERTIFICATE-----
MIICuDCCAaCgAwIBAgIEXqvo6jANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDDApP
...
xIuwGz9DE9uQYyE4s1kkPMf//6JKTJbEH7uTxCTinIugM666OB6aeWxhLRwCNUPN
ICe5azP9eGeUzKBJaIwEQGchAMLBSxTsm2Bkqg==
-----END CERTIFICATE-----
</ca>

<cert>
-----BEGIN CERTIFICATE-----
MIICyzCCAbOgAwIBAgIBAzANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDDApPcGVu
VlBOIENBMB4XDTIwMDQyNDA5NTIxOFoXDTMwMDQyOTA5NTIxOFowGzEZMBcGA1UE
...
ggEBAKxp+gqIFDtvLC46XsAzgG5Dm99niPYxWgRfwvy6aXPBfU5q9e6Hae5SnqXy
+jUE8rcvUtV3garpOTSkkYXVqDmCorT+doinN9oi3yge5n0G6JHo0XUnS1Ke+h8=
-----END CERTIFICATE-----
</cert>

<key>
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCsafoKiBQ7bywu
...
o8ZOoXvWbgCOVBLufmoLthaqXUrbX0bJWfn+I3aDiN2eHRZmcBFVWc+vhcRce+7Y
```

##### 2.5 Delete Target OpenVpn client profile file

|                      | Value                                          | Remark                                                       |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| End Point            | /api/v1/openvpn/profile?filename=myclient.ovpn | query string with field name : filename, and value contain full file name you upload. |
| Method               | DELETE                                         |                                                              |
| Header: mx-api-token | {API token}                                    | Restful API access token                                     |

Request Example:

```
curl https://192.168.8.202:8443/api/v1/openvpn/profile?filename=myclient.ovpn \
-X DELETE -H "Content-Type:application/json" \
-H "mx-api-token:$(cat /var/thingspro/data/mx-api-token)" -k
```

Response Example:

```
{
    "message": "Delete config successfully"
}
```

### 3. Troubleshooting

##### 3.1 OpenVPN Version

The client version can be found with the following command. Please make sure not to contain incompetible OpenVPN settings introduced from OpenVPN v2.5+ in our ovpn file.

```
root@Moxa:/home/moxa# docker exec -it openvpn_app_1 openvpn --version
OpenVPN 2.4.0 arm-unknown-linux-gnueabihf [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Oct 14 2018
library versions: OpenSSL 1.0.2u  20 Dec 2019, LZO 2.08
Originally developed by James Yonan
Copyright (C) 2002-2017 OpenVPN Technologies, Inc. <sales@openvpn.net>
Compile time defines: enable_async_push=no enable_comp_stub=no enable_crypto=yes enable_crypto_ofb_cfb=yes enable_debug=yes enable_def_auth=yes enable_dependency_tracking=no enable_dlopen=unknown enable_dlopen_self=unknown enable_dlopen_self_static=unknown enable_fast_install=yes enable_fragment=yes enable_iproute2=yes enable_libtool_lock=yes enable_lz4=yes enable_lzo=yes enable_maintainer_mode=no enable_management=yes enable_multi=yes enable_multihome=yes enable_pam_dlopen=no enable_password_save=yes enable_pedantic=no enable_pf=yes enable_pkcs11=yes enable_plugin_auth_pam=yes enable_plugin_down_root=yes enable_plugins=yes enable_port_share=yes enable_selinux=no enable_server=yes enable_shared=yes enable_shared_with_static_runtimes=no enable_silent_rules=no enable_small=no enable_static=yes enable_strict=no enable_strict_options=no enable_systemd=yes enable_werror=no enable_win32_dll=yes enable_x509_alt_username=yes with_crypto_library=openssl with_gnu_ld=yes with_mem_check=no with_plugindir='${prefix}/lib/openvpn' with_sysroot=no
```

##### 3.2 OpenVPN Log

If the OpenVPN client is not working properly, logs can be printed out with the following command.

```
root@Moxa:/home/moxa# docker exec -it openvpn_app_1 tail -n 100 /var/log/openvpn/openvpn.log
```