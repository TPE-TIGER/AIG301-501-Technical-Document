# thingspro-agent Release & Configuration

  Document Version: 1.2

  ### Change Log

  | Version | Date       | Content         |
  | ------- | ---------- | --------------- |
  | 1.1     | 2023-01-19 | version update. |
  | 1.2     | 2023-02-01 | AIG series.     |

  ### AIG-301 Device

  | AIG Version | IoT Edge Version | thingspro-agent version | Module URL                           | Create Option                                                |
  | ----------- | ---------------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
  | 1.4         | 1.2.7            | 2.2.2                   | moxa2019/thingspro-agent:2.2.2-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.3         | 1.1.4            | 2.2.2                   | moxa2019/thingspro-agent:2.2.2-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.2         | 1.0.10           | 2.1.1                   | moxa2019/thingspro-agent:2.1.1-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/cloud/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |

  ### AIG-501 Device

  | AIG Series | IoT Edge Version | thingspro-agent version | Module URL                           | Create Option                                                |
  | ---------- | ---------------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
  | 1.2        | 1.2.7            | 2.2.2                   | moxa2019/thingspro-agent:2.2.2-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.1        | 1.1.4            | 2.2.2                   | moxa2019/thingspro-agent:2.2.2-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |

> Note: We were previously recommending thingspro-agent:2.2.3 instead of thingspro-agent:2.2.2 on this page, the difference between these two versions is that thingspro-agent:2.2.3 is leveraging a newer version of Azure IoT SDK (LTS_07_2020_Ref02 -> LTS_01_2023_Ref01). To avoid confusion, we are rolling back the recommended version to thingpro-agent:2.2.2, which matches the user manual. \
> If you encounter issues while using thingspro-agent:2.2.2 and feel like the issue is being fixed in the newer Azure SDK version, thingspro-agent:2.2.3 may still be worth trying.
