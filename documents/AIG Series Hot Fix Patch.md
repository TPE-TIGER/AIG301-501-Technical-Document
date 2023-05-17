# AIG Series Hot Fix Patch

Document Version: 1.0

### Change Log

| Version | Date       | Content                 |
| ------- | ---------- | ----------------------- |
| 1.0     | 2023-05-17 | Add Web UI 1.40.42-6517 |



| Hot Fix Name             | edge-web_1.40.42-6517_armhf.mpkg                             |
| ------------------------ | ------------------------------------------------------------ |
| Issue Solved             | Admin Web UI can't display correctly when PC/Laptop without Internet access. |
| Date                     | 2023-05-17                                                   |
| Download URL             | https://tpe2.azureedge.net/HotFix/edge-web_1.40.42-6517_armhf.mpkg |
| Tested Devices & Version | AIG-301 1.4                                                  |
| Known Issue              | The map diagram can't display.                               |
| Installation Step        | 1. Download mpkg file from above link.<br />2. SSH login to AIG device.<br />3. Switch as su or root<br />4. Run command: appman app install edge-web_1.40.42-6517_armhf.mpkg |
| Note                     | 1. You may need to purge browser's cache or open an incognito mode browser. |

