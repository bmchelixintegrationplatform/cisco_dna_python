# Cisco DNA Center Trigger Issues


This Python script will disable a network device interface that will trigger an Assurance issue in DNA Center

**Cisco Products & Services:**

- Cisco DNA Center
- Cisco Network Devices Managed by Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

Run the script {create_interface_event.py}.

It will disable a network interface for 60 seconds and enable the interface. 

This time interval is sufficient to send a notification out from Cisco DNA Center.

After interface is enabled, a second notification will be sent out with the issue status "resolved"

**Sample Output**



**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
