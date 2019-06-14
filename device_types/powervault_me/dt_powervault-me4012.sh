#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerVault ME4012", slug="powervault-me4012").save()
dt = DeviceType.objects.get(slug="powervault-me4012")
dt.u_height="2"
dt.save()

quit()
EOF