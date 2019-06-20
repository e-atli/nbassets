#!/bin/bash

echo "Creating Netbox Assets"
echo "======================"
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo

echo "Searching Cluster Types"
echo "======================="
find cluster_types -name ct_*
echo
echo "Processing..."
#python3 $NETBOX_PATH/manage.py nbshell <python/manufacturers.py
python3 $NETBOX_PATH/manage.py nbshell <python/cluster_types.py > /dev/null 2>&1

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
python3 $NETBOX_PATH/manage.py nbshell <python/device_types.py
#python3 $NETBOX_PATH/manage.py nbshell <python/device_types.py > /dev/null 2>&1

echo
echo "Searching Device Roles"
echo "======================"
find device_roles -name dr_*
echo
echo "Processing..."
#python3 $NETBOX_PATH/manage.py nbshell <python/device_roles.py
python3 $NETBOX_PATH/manage.py nbshell <python/device_roles.py > /dev/null 2>&1

echo
echo "Done."
