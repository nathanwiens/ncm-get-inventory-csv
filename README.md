# ncos-get-inventory-csv

This script will generate a CSV file of router inventory along with specified configuration items.

It currently populates:
'ROUTER NAME', 'SERIAL NUMBER', 'GRE 1 IP', 'GRE 2 IP', 'BGP ROUTER ID', 'SUBNET 1 IP', 'SUBNET 2 IP'

To run:
1. Set API Keys and Account ID in config.py
2. Run 'python3 get_inventory_csv.py'
