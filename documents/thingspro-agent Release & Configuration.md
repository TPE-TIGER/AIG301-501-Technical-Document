# thingspro-agent Release & Configuration

  Document Version: 1.2

  ### Change Log

  | Version | Date       | Content         |
  | ------- | ---------- | --------------- |
  | 1.5     | 2025-07-07 | AIG-301 v1.7.   |
  | 1.4     | 2024-11-12 | AIG-301 v1.6 and AIG-501 v1.4. |
  | 1.3     | 2024-04-08 | AIG-301 v1.5 security patch and AIG-501 v1.3. |
  | 1.2     | 2023-09-26 | AIG-301 v1.5.   |
  | 1.2     | 2023-02-01 | AIG series.     |
  | 1.1     | 2023-01-19 | version update. |

  ### AIG-301 Device

  | AIG Version | IoT Edge Version | thingspro-agent version | Module URL                           | Create Option                                                |
  | ----------- | ---------------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
  | 1.7         | 1.4.40           | 2.2.6                   | moxa2019/thingspro-agent:2.2.6-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.6         | 1.4.40           | 2.2.6                   | moxa2019/thingspro-agent:2.2.6-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.5         | 1.4.10           | 2.2.5                   | moxa2019/thingspro-agent:2.2.5-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.5         | 1.4.10           | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.4         | 1.2.7            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.3         | 1.1.4            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.2         | 1.0.10           | 2.1.1                   | moxa2019/thingspro-agent:2.1.1-armhf | { "HostConfig": { "Binds": [ "/var/thingspro/apps/cloud/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |

### Note
> thingspro-agent version 2.2.5 is released for security issues, please refer to [Security patch for AIG -301 v1.5](./AIG%20Software%20Upgrade.md#security-patch-for-aig-301-version-15).

  ### AIG-501 Device

  | AIG Series | IoT Edge Version | thingspro-agent version | Module URL                           | Create Option                                                |
  | ---------- | ---------------- | ----------------------- | ------------------------------------ | ------------------------------------------------------------ |
  | 1.4         | 1.4.40           | 2.2.6                   | moxa2019/thingspro-agent:2.2.6-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.3        | 1.4.20           | 2.2.4                   | moxa2019/thingspro-agent:2.2.4-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.2        | 1.2.7            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |
  | 1.1        | 1.1.4            | 2.2.3                   | moxa2019/thingspro-agent:2.2.3-amd64 | { "HostConfig": { "Binds": [ "/var/thingspro/apps/azureiotedge/data/setting/:/var/thingspro/cloud/setting/", "/run/:/host/run/", "/var/thingspro/data/:/var/thingspro/data/" ] } } |

### Note
> By customer's feedback and community's testing, thingspro-agent: 2.2.2 has known issue on sending device to cloud message. So, at here, we recommand to using thingspro-agent:2.2.3.
