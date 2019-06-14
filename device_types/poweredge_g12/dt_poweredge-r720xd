#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R720xd", slug="poweredge-r720xd").save()
dt = DeviceType.objects.get(slug="poweredge-r720xd")
dt.u_height="2"
dt.save()

quit()
EOF