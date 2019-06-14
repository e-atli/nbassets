#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge T420", slug="poweredge-t420").save()
dt = DeviceType.objects.get(slug="poweredge-t420")
dt.u_height="5"
dt.save()

quit()
EOF