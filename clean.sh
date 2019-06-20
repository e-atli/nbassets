#!/bin/bash

echo "Cleaning Netbox Assets"
echo "======================"
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo

echo "Cleaning all unused Types, Roles, Manufacturers..."
echo
python3 $NETBOX_PATH/manage.py nbshell <python/clean.py
#python3 $NETBOX_PATH/manage.py nbshell <python/clean.py > /dev/null 2>&1

echo
echo "Done."
