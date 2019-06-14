#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerEdge R830", slug="poweredge-r830").save()
dt = DeviceType.objects.get(slug="poweredge-r830")
dt.u_height="2"
dt.save()

quit()
EOF