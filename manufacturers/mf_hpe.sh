#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF
Manufacturer(slug="hpe", name="HPE").save()
quit()
EOF