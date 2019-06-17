manufacturer_id = Manufacturer.objects.get(slug="dell-emc").id

DeviceType(slug="poweredge-t320", manufacturer_id=manufacturer_id).save()

DeviceType = DeviceType.objects.get(slug="poweredge-t320")
DeviceType.model="PowerEdge T320"
DeviceType.u_height="5"
DeviceType.is_full_height=True
DeviceType.save()

PowerPortTemplate(device_type_id=DeviceType.id, name="PS1").save()
PowerPortTemplate(device_type_id=DeviceType.id, name="PS2").save()

InterfaceTemplate(device_type_id=DeviceType.id, name="iDRAC").save()

InterfaceTemplate = InterfaceTemplate.objects.get(device_type_id=DeviceType.id, name="iDRAC")
InterfaceTemplate.form_factor="1000"
InterfaceTemplate.mgmt_only=True
InterfaceTemplate.save()
