#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R220", slug="poweredge-r220").save()
dt = DeviceType.objects.get(slug="poweredge-r220")
dt.u_height="1"
dt.save()

quit()
EOF