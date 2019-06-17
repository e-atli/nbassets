MFGSLUG = "dell-emc"
SLUG = "poweredge-r620"
MODEL = "PowerEdge R620"
U_HEIGHT = "1"
IS_FULL_HEIGHT = True

PowerPortTemplate(device_type_id=DeviceType.id, name="PS1").save()
PowerPortTemplate(device_type_id=DeviceType.id, name="PS2").save()

InterfaceTemplate(device_type_id=DeviceType.id, name="iDRAC").save()

InterfaceTemplate = InterfaceTemplate.objects.get(device_type_id=DeviceType.id, name="iDRAC")
InterfaceTemplate.form_factor="1000"
InterfaceTemplate.mgmt_only=True
InterfaceTemplate.save()
