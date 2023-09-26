# thingspro-agent Release & Configuration

  Document Version: 1.2

  ### Change Log

  | Version | Date       | Content         |
  | ------- | ---------- | --------------- |
  | 1.1     | 2023-01-19 | version update. |
  | 1.2     | 2023-02-01 | AIG series.     |
  | 1.2     | 2023-09-26 | AIG-301 v1.5.   |

  ### AIG-301 Device

  | AIG Version | IoT Edge Version | thingspro-agent version | Module URL                           | Create Option                                                |
  | ----------- | ---------------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
  | 1.5         | 1.4.10            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.4         | 1.2.7            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.3         | 1.1.4            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.2         | 1.0.10           | 2.1.1                   | moxa2019/thingspro-agent:2.1.1-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/cloud/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |

  ### AIG-501 Device

  | AIG Series | IoT Edge Version | thingspro-agent version | Module URL                           | Create Option                                                |
  | ---------- | ---------------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
  | 1.2        | 1.2.7            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.1        | 1.1.4            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |

### Note
> By customer's feedback and community's testing, thingspro-agent: 2.2.2 has known issue on sending device to cloud message. So, at here, we recommand to using thingspro-agent:2.2.3.
