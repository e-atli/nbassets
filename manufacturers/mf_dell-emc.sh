#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF
Manufacturer(slug="dell-emc", name="Dell EMC").save()
quit()
EOF