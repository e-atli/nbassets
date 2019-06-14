#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R930", slug="poweredge-r930").save()
dt = DeviceType.objects.get(slug="poweredge-r930")
dt.u_height="4"
dt.save()

quit()
EOF