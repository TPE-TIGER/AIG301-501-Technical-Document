# ThingsPro Edge V2 Benchmark & Limitation

​	

### Software Upgrade

##### **Software upgrade with snapshot**

| Step | Task                                   | Duration                                 |
| ---- | -------------------------------------- | ---------------------------------------- |
| 1    | Download Software                      | depend on network bandwidth              |
| 2    | Take snapshot                          | ~13 min                                  |
| 3    | Installation                           | ~15 min                                  |
| 4    | Restart                                | ~2 min                                   |
|      | <font color='blue'><b>Total</b></font> | <font color='blue'><b>~30 min</b></font> |

##### **Software upgrade without snapshot**

| Step | Task                                   | Duration                                 |
| ---- | -------------------------------------- | ---------------------------------------- |
| 1    | Download Software                      | depend on network bandwidth              |
| 2    | Installation                           | ~13 min                                  |
| 3    | Restart                                | ~2 min                                   |
|      | <font color='blue'><b>Total</b></font> | <font color='blue'><b>~15 min</b></font> |

##### **Roll back from snapshot if fail**

| Step | Task                                   | Duration |
| ---- | -------------------------------------- | -------- |
| 1    | Roll Back                              | ~ 5 min  |
| 2    | Restart                                | ~2 min   |
|      | <font color='blue'><b>Total</b></font> |          |



### Modbus Master Limitation

| Item                           | Max Value | Note                                                |
| ------------------------------ | --------- | --------------------------------------------------- |
| Max Serial Slave Device #      | 31        | Able to create max 31 serial slave device.          |
| Max TCP Slave Device #         | 32        | Able to create max 32 TCP slave device.             |
| Max Command #                  | 2048      | Support max 2048 commands across all slave devices. |
| Max Tag #                      | 2048      | Support max 2048 tags across all commands.          |
| Max Command # in a Serial Port | 128       | Support max 128 commands for a serial slave device. |
| Max Command # in a TCP Port    | 2048      | Support max 2048 commands for a TCP slave device.   |

Modbus Master application support big integer range are:

| Data Type      | Min              | Max                   |
| -------------- | ---------------- | --------------------- |
| Int64          | -922337203685477 | 922337203685477       |
| Unsigned int64 | 0                | 1,844,674,407,370,954 |



