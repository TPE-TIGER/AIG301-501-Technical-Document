# Enforce Secured Setting on ThingsPro Edge

Document Version: V1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-04-11 | document created. |

### Purpose

This document lists out the recommended actions to be taken in Debian OS before deployments, to further secure IIoT gateways that are runnning ThingsPro Edge in the field.

---

### 1. Secured User Access

All Moxa's industrial conputers share the same default username and password, which is publically available to everyone in the user manual and should be disabled before deployments. We encourge users to secure your system by creating new accounts and remove the default one, while making sure that suitable password complexity is applied, or even consider introducing PAM (Pluggable Authentication Modules) to the system.

### 2. SSH Settings

Although ThingsPro Edge disables SSH server by default, we might still have to enable it under certain circumstances. That said, it could still be valueable to ensure SSH server is properly configured. For more information about how to configure SSH server, please refer to its [online document](https://manpages.debian.org/stretch/openssh-server/sshd_config.5.en.html).

### 3. Preventing Brute Force Attacks

Setting up MaxAuthTries in sshd_config is often not enough to keep the unit from the risk of being brute force attacked. We can further protect our devices by running tools such as Fail2ban on the system.

### 4. Shell Timeout

It could also be beneficial to setup shell timeout for users with the TMOUT variable when SSH connections are enabled. 

### 5. System Settings

Do not configure settings that can be configured through ThingsPro Edge via command line. ThingsPro Edge configures the system based on its own configuration files and thus overwrites those system settings.

### 6. Keeping the System Up-to-Date

Periodically upgrading the system with APT command is a good practice to ensure that the device has all the latest security patches installed.

### 7. Third-Party Software

Users must understand that installing third-party software on a deployed unit is a high risk action which may cause unexpected result. We do not recommend users to do so without thoroughly tested in the lab and the responsibility of validating the software falls on the users.

### 8. Validate the Hardware Wirings

We can't expect the gateway to function properly if it's not being wired correctly. The most common issue we've seen in the past is related to the cellular antenna.

1. Use the correct type (male/female) of antenna.
2. Carefully read the manual and connect the antennas to the right ports. **Do not mess up with the GPS port**.
3. Both the primary and the auxiliary antenna are required.
