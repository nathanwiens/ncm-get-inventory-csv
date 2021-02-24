"""IMPORT DEPENDENCIES"""
import config
import ncm
from csv import writer
from datetime import date

"""
####################################################################################################
# GET NCM ROUTER INVENTORY
# Created by Nathan Wiens (nathan@wiens.co)
#
# MIT License
#
# Copyright (c) 2021 Nathan Wiens
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
####################################################################################################
"""

n = ncm.NcmClient(config.api_keys, logEvents=False)
account_id = config.account_id

today = date.today().strftime("%Y-%m-%d")

csv_header = ['ROUTER NAME', 'SERIAL NUMBER', 'GRE 1 IP', 'GRE 2 IP', 'BGP ROUTER ID', 'SUBNET 1 IP', 'SUBNET 2 IP']

filename = 'Cradlepoint_GRE_IPs_{}.csv'.format(today)

with open(filename, 'w', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(csv_header)

    for router in n.get_routers():
        data = ['', '', '', '', '', '', '']
        configman = n.get_configuration_managers(router=router['id'])
        if 'gre' in configman[0]['configuration'][0]:

            data[0] = router['name']
            data[1] = router['serial_number']
            for k, v in configman[0]['configuration'][0]['gre']['tunnels'].items():
                if '00000000' in k:
                    data[2] = v['local_network']
                if '00000001' in k:
                    data[3] = v['local_network']
            data[4] = configman[0]['configuration'][0]['routing']['bgp']['routers']['0']['router_id']
            for k, v in configman[0]['configuration'][0]['lan'].items():
                if '00000000' in k:
                    data[5] = v['ip_address']
                if '00000001' in k:
                    data[6] = v['ip_address']

            # Add contents of list as last row in the csv file
            csv_writer.writerow(data)
