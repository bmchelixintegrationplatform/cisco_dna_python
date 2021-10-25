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


import json
import xml
import xml.dom.minidom
import urllib3
import lxml.etree as et
import requests
import xmltodict
from ncclient import manager
from ncclient.operations import RPCError
from requests.auth import HTTPBasicAuth  # for Basic Auth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def netconf_oper_admin_interface(interface, admin_status, ios_xe_host, ios_xe_port, ios_xe_user, ios_xe_pass):
    """
    This function will retrieve the IPv4 address configured on the interface via NETCONF
    :param interface: interface name
    :param admin_status: interface admin status {True/False}
    :param ios_xe_host: device IPv4 address
    :param ios_xe_port: NETCONF port
    :param ios_xe_user: username
    :param ios_xe_pass: password
    :return oper_status: the interface operational status - up/down
    """
    with manager.connect(host=ios_xe_host, port=ios_xe_port, username=ios_xe_user,
                         password=ios_xe_pass, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        # XML filter to issue with the get operation
        # IOS-XE 16.6.2+        YANG model called "ietf-interfaces"

        interface_filter = '''
            <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                      <name>''' + interface + '''</name>
                      <enabled>''' + admin_status + '''</enabled>
                    </interface>
                </interfaces>
            </config>
        '''
        # execute NETCONF operation
        try:
            response = m.edit_config(target='running', config=interface_filter)
            response_str = json.dumps(xmltodict.parse(str(response)))
            if 'ok' in response_str:
                data = 'success'
        except RPCError as e:
            data = e._raw
        return data

