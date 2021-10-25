#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import datetime
import config
import urllib3
import utils

from netmiko import ConnectHandler
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

from config import IOS_XE_HOST, IOS_XE_USER, IOS_XE_PASS

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


date_time = str(datetime.datetime.now().replace(microsecond=0))

print('\nApplication "create_interface_event.py" started ', date_time)

DEVICE_INFO = {
    'device_type': 'cisco_ios',
    'host': IOS_XE_HOST,
    'username': IOS_XE_USER,
    'password': IOS_XE_PASS,
    'secret': IOS_XE_PASS
    }

interface_number = 'TenGigabitEthernet1/1/3'


# connect to device using ssh/netmiko
net_connect = ConnectHandler(**DEVICE_INFO)
net_connect.enable()

command_output = net_connect.find_prompt()
print('\nPrompt of the connected device: ', command_output)

# define the config command sets to be sent to device.
config_commands = [
                   'interface ' + interface_number,
                   'shutdown'
                   ]
# send config commands to device
commands_output = net_connect.send_config_set(config_commands)
print('\nCommands sent: ', commands_output)

# wait for event to be created
utils.time_sleep(120)

# define the config command sets to be sent to device.
config_commands = [
                   'interface ' + interface_number,
                   'no shut'
                  ]
# send config commands to device
commands_output = net_connect.send_config_set(config_commands)
print('\nCommands sent: ', commands_output)

print('Application "create_interface_event.py" run end')
