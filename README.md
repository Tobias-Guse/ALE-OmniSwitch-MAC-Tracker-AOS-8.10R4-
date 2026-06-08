# OmniSwitch MAC Tracker (AOS 8.10R4)

Simple Python script for tracking a specific MAC address on an Alcatel-Lucent Enterprise OmniSwitch running AOS 8.10R4.

The script continuously polls the MAC address table every second and logs:

 Timestamp
 VLAN
 Switch port
 MAC move events



# Features

 Continuous MAC tracking
 1-second polling interval
 VLAN detection
 Port detection
 Log rotation
 Lightweight and easy to deploy
 Compatible with OmniSwitch AOS 8.x / 8.10R4



# Example Output

```text
[2026-06-08 10:20:01.125] #000001 | port = 1/1/11 | vlan = 1000
[2026-06-08 10:20:02.231] #000002 | port = 1/1/11 | vlan = 1000
[2026-06-08 10:20:03.337] #000003 | port = 1/1/12 | vlan = 1000
```

This makes it easy to detect:

 MAC flapping
 Device movement
 Physical switch port changes
 Loop situations



# Requirements

 OmniSwitch AOS 8.10R4
 Python installed on the switch
 CLI access



# Installation

Copy the script to the switch:

```bash
/flash/mac_tracker.py
```

Make the script executable:

```bash

python3 mac_tracker.py
```



# Configuration

Edit the MAC address inside the script:

```python
MAC_ADDRESS = "44:1e:a1:3b:13:0c"
```

Optional settings:

```python
POLL_INTERVAL = 1
LOG_FILE = "/flash/mac_tracker.log"
```



# Start the Script

```bash
python /flash/working/mac_tracker.py &
```

Run in background.



# Stop the Script

Find process:

```bash
ps | grep mac_tracker
```

Kill process:

```bash
kill <PID>
```



# View Live Logs

```bash
tail -f /flash/mac_tracker.log
```



# Log Rotation

Automatic log rotation starts when the logfile exceeds:

```text
5 MB
```

Backup logfile:

```text
/flash/mac_tracker.log.1
```



# Tested On

 OmniSwitch 6860
 AOS 8.10R4



# Use Cases

 Troubleshooting MAC flapping
 Tracking unknown devices
 Identifying physical switch ports
 Detecting unstable links
 Monitoring device movement in datacenter environments



# Disclaimer

This script is provided as-is without warranty.  
Test in a lab environment before using in production systems.



