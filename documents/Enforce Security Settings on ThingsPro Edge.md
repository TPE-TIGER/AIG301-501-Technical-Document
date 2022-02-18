# Enforce Secured Setting on ThingsPro Edge

Document Version: V1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2022-02-18 | document created. |

### 1. Purpose

This document lists out the recommended actions to be taken in ThingsPro Edge before deplyments, to secure IIoT gateways in the field.

---

### 1.1 Manage Roles and Users

The user should be aware that information containing the default account and password is publically available to everyone, and thus it should only be used for the purpose of installation.

#### 1.2 Create New Roles and Users

It's recommended to create new user accounts for each individual with adequate permissions. In ThingsPro Edge, permissions can be grouped as roles, then further assigned to user accounts. 

#### 1.3 Disable or Change the Password for Default Account

Once user accounts have been created, user should either remove the default account, or change the default password of it. 

> Note: To avoid from being unintentionallty locked out from the gateway, ThingsPro Edge does not allow the last user account assigned administrator role to be removed.

### 2. Disable Unused Interfaces

The user should disable unused interfaces to prevent unexpected access to the gateway.

> Note: The user must realize that although the gateway has become more secured by disabling unused interfaces, the tradeoff is it's resilience because the backup options to access the gateway have been disabled.

#### 2.1 SD Card

ThingsPro Edge disables SD card by default. The user should enable it only when required, and do not storing sensitive data on it to mitigate the risk of losing it.

#### 2.2 Web Service

ThingsPro Edge enables HTTPS for gateway initialization by default. The user should disable it once the gateway has been properly configured to prevent unexpected access.

#### 2.3 Console Port

ThingsPro Edge leaves console port enabled by default for debug purpose. The user should disable it before deploying the gateway to an unattended location.

#### 2.4 SSH Server

ThingsPro Edge disables SSH server by default. It's common that the user may enable it to gain further control for device initialization. However, it should be disabled once the gateway has been properly configured to prevent unexpected access.

### 3. Configure the System

The user should have the security related settings properly setup to enhance gateway security.

#### 3.1 Time

System time is widely used in security related actions, such as certificate validation. The user should configure system time properly and enable auto sync if possible.

#### 3.2 HTTPS

If, for some reason, the user decides to leave https service enabled in the field, it's recommended to import your own certificate and private key for the HTTPS service, so user's working laptop can successfully validate the identity of the gateway.

The HTTPS service on ThingsPro Edge comes with a set of self-signed certificate and private key by default. If the user is not able to replace the default with your own certificate and private key, we recommend the user to export the default root certificate from ThingsPro Edge and add it to the trusted root certificate authority list on your working laptop.

#### 3.3 Firewall

ThingsPro Edge accepts all output traffic while exposes only the 8443 port for HTTPS service. The user may consider rejecting outbound traffic designated to certain IP addresses based on your need, and only expose more inbound ports if necessary.
