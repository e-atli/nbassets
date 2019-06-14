#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerVault MD3220", slug="powervault-md3220").save()
dt = DeviceType.objects.get(slug="powervault-md3220")
dt.u_height="2"
dt.save()

quit()
EOF