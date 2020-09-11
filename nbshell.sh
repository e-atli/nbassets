#!/bin/bash

# 2020-09-11 Update script to use VENV

echo "Starting Netbox Shell"
echo "====================="
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo
echo "Type quit() to exit."

# Before running nbshell, enter venv
if [ -e "$NETBOX_PATH/../venv/bin/activate" ];
  then
    {
      echo
      echo "VENV binary detected. Entering VENV..."
      source $NETBOX_PATH/../venv/bin/activate
    }
  else
    {
      echo
      echo "Not using venv."
    }
fi

# Enter Netbox shell
python3 $NETBOX_PATH/manage.py nbshell
echo
echo "Done."

# Exit VENV
if [ $VIRTUAL_ENV != '' ];
  then
    echo "Leaving VENV..."
    deactivate;
fi
