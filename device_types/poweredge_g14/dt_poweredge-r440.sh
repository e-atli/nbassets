#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R440", slug="poweredge-r440").save()
dt = DeviceType.objects.get(slug="poweredge-r440")
dt.u_height="1"
dt.save()

quit()
EOF
