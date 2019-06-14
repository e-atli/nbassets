#!/bin/sh

python3 $NETBOX_PATH/manage.py nbshell <<EOF

mnid = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(manufacturer_id=mnid, model="PowerVault MD3400", slug="powervault-md3400").save()
dt = DeviceType.objects.get(slug="powervault-md3400")
dt.u_height="2"
dt.save()

quit()
EOF