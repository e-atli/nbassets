#!/bin/bash

echo "Cleaning Netbox Assets"
echo "======================"
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo

echo "Cleaning all unused Cluster Types..."
echo "Cleaning all unused Device Roles..."
echo "Cleaning all unused Device Types..."
echo "Cleaning all unused Manufacturers..."
python3 $NETBOX_PATH/manage.py nbshell <python/clean.py > /dev/null 2>&1

echo
echo "Done."
