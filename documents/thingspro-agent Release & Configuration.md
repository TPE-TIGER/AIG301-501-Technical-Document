# thingspro-agent Release & Configuration

Document Version: 1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-02-19 | document created. |



| TPE Version | thingspro-agent version | Module URL                                                   | Create Option                                                |
| ----------- | ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2.3.0       | 2.2.2                   | `moxa2019/thingspro-agent:2.2.2-amd64`<br />`moxa2019/thingspro-agent:2.2.2-armhf` | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |
| 2.2.1       | 2.2.2                   | `moxa2019/thingspro-agent:2.2.2-amd64`<br />`moxa2019/thingspro-agent:2.2.2-armhf` | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |
| 2.2.0       | 2.1.1                   | `moxa2019/thingspro-agent:2.1.1-amd64`<br />`moxa2019/thingspro-agent:2.1.1-armhf` | {  "HostConfig": {    "Binds": [        "/var/thingspro/apps/cloud/data/setting/:/var/thingspro/cloud/setting/",        "/run/:/host/run/",        "/var/thingspro/data/:/var/thingspro/data/"    ]  } } |



##### Related documents：

- [ThingsPro Edge Software Release & Download](ThingsPro Edge Software Release.md)
