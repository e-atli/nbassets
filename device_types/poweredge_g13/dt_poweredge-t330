#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge T330", slug="poweredge-t330").save()
dt = DeviceType.objects.get(slug="poweredge-t330")
dt.u_height="5"
dt.save()

quit()
EOF