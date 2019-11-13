#!/bin/bash

echo "Starting Netbox Shell"
echo "====================="
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo
echo "Type quit() to exit."

python3 $NETBOX_PATH/manage.py nbshell

echo "Done."
