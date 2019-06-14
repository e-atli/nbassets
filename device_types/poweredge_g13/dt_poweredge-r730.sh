#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R730", slug="poweredge-r730").save()
dt = DeviceType.objects.get(slug="poweredge-r730")
dt.u_height="2"
dt.save()

quit()
EOF