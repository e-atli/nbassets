#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R520", slug="poweredge-r520").save()
dt = DeviceType.objects.get(slug="poweredge-r520")
dt.u_height="2"
dt.save()

quit()
EOF