#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerVault ME4024", slug="powervault-me4024").save()
dt = DeviceType.objects.get(slug="powervault-me4024")
dt.u_height="2"
dt.save()

quit()
EOF