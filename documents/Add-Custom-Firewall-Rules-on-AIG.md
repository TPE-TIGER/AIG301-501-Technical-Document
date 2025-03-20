# Add Custom Firewall Rules on AIG

Document Version: V1.0

### Change Log

| Version | Date       | Content           |
| ------- | ---------- | ----------------- |
| 1.0     | 2025-03-19 | document created. |

##### Applicable Products
| Product | Version |
| ------- | ------- |
| AIG-301 | 1.5.0+  |
| AIG-501 | 1.3.0+  |

## Purpose

The built-in firewall settings in the product only support basic allow and forward rules. However, since the system manages firewall rules using chains, users can apply custom rules outside of the predefined chains without interference from the system.

This document provides guidance on how to configure additional firewall rules while ensuring compatibility with the system’s built-in settings.

## Steps

1. Create a iptables rules file. The following example rejects packets from wwan0 to port 1883.
    ```bash
    $ sudo cat /etc/iptables/up-custom-user.rules
    *filter
    :CUSTOM-USER - [0:0]
    -A CUSTOM-USER -i wwan0 -p tcp -m tcp --dport 1883 -j REJECT
    COMMIT
    ```
    Modify the chain (`CUSTOM-USE`) in the example as needed.
    > Note: 
    > - Chains with the prefix `MOXA-` may be used by the system. Please avoid using them to prevent rules from being flushed unexpectedly.
    > - You can place the rules file (the previous example is `/etc/iptables/up-custom-user.rules`) in any path that is convenient for later management.

2. Edit `/etc/rc.local` to write the rules into iptables.
    ```bash
    $ sudo cat /etc/rc.local
    #!/bin/sh -e
    #
    # rc.local
    #
    # This script is executed at the end of each multiuser runlevel.
    # Make sure that the script will "exit 0" on success or any other
    # value on error.
    #
    # In order to enable or disable this script just change the execution
    # bits.
    #
    # By default this script does nothing.
    iptables-restore --noflush < /etc/iptables/up-custom-user.rules
    ```
    > Replace the sample rules file `/etc/iptables/up-custom-user.rules` with your own.

3. Enable `rc-local` service to make sure the firewall rules apply after booting.
    ```bash
    $ sudo systemctl enable rc-local
    ```

> `ip_forward`  (`echo 1 > /proc/sys/net/ipv4/ip_forward`) already enabled by system.

## Examples

### Allows only LAN1 (eth1) to access TCP port 8443

#### Rule File
```iptables.rules
*filter
:INPUT - [0:0]
-I INPUT 1 -p tcp -i eth1 --dport 8443 -j ACCEPT
-I INPUT 2 -p tcp --dport 8443 -j DROP
COMMIT
```

#### Description
The first rule is to accept packets to port 8443 from a specific interface:
```
-I INPUT <index> -p tcp -i <source-interface> --dport 8443 -j ACCEPT
```

If address should be used, use `-s <source-address>` instead of `-i <source-interface>` to accept packets from assigned source address.


The second rule is to drop all other packets to port 8443:
```
-I INPUT <index+1> -p tcp --dport 8443 -j DROP
```

> Please note that the index is required in the rules to ensure that the packet is processed before being accepted by the AIG.