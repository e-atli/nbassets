#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge MD3200", slug="poweredge-md3200").save()
dt = DeviceType.objects.get(slug="poweredge-md3200")
dt.u_height="2"
dt.save()

quit()
EOF