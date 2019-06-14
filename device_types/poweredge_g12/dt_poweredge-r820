#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R820", slug="poweredge-r820").save()
dt = DeviceType.objects.get(slug="poweredge-r820")
dt.u_height="2"
dt.save()

quit()
EOF