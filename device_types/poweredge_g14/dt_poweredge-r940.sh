#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R940", slug="poweredge-r940").save()
dt = DeviceType.objects.get(slug="poweredge-r940")
dt.u_height="4"
dt.save()

quit()
EOF