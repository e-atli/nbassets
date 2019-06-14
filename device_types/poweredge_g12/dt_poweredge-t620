#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge T620", slug="poweredge-t620").save()
dt = DeviceType.objects.get(slug="poweredge-t620")
dt.u_height="5"
dt.save()

quit()
EOF