# thingspro-agent Release & Configuration

Document Version: 1.2

### Change Log

| Version | Date       | Content         |
| ------- | ---------- | --------------- |
| 1.1     | 2023-01-19 | version update. |
| 1.2     | 2023-02-01 | AIG series.     |



### AIG-301 Device

| AIG Version | thingspro-agent version | Module URL                           | Create Option                                                |
| ----------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
| 1.4         | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |
| 1.3         | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |
| 1.2         | 2.1.1                   | moxa2019/thingspro-agent:2.1.1-armhf | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/cloud/data/setting/:/var/thingspro/cloud/setting/",                "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |



### AIG-501 Device

| AIG Series | thingspro-agent version | Module URL                           | Create Option                                                |
| ---------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
| 1.2        | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-amd64 | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |
| 1.1        | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-amd64 | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |



##### Related documents：

- [ThingsPro Edge Software Release & Download](ThingsPro%20Edge%20Software%20Release.md)
