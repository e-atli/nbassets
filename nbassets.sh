#!/bin/bash

echo "Creating Netbox Assets"
echo "======================"
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo

echo "Searching Manufacturers"
echo "======================="
find manufacturers -name mf_*
echo
echo "Processing..."
#python3 $NETBOX_PATH/manage.py nbshell <python/manufacturers.py
python3 $NETBOX_PATH/manage.py nbshell <python/manufacturers.py > /dev/null 2>&1

echo
echo "Searching Device Types"
echo "======================"
find device_types -name dt_*
echo
echo "Processing..."
#python3 $NETBOX_PATH/manage.py nbshell <python/device_types.py
python3 $NETBOX_PATH/manage.py nbshell <python/device_types.py > /dev/null 2>&1

echo
echo "Done."

