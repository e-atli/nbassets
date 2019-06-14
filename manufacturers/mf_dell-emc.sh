#!/bin/sh

python3 manage.py nbshell <<EOF
Manufacturer(slug="dell-emc", name="Dell EMC").save()
quit()
EOF

