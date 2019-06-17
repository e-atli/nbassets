MFGSLUG = "dell-emc"
SLUG = "poweredge-t620"
MODEL = "PowerEdge T620"
U_HEIGHT = "5"
IS_FULL_DEPTH = True

PowerPortTemplate(device_type_id=DeviceType.id, name="PS1").save()
PowerPortTemplate(device_type_id=DeviceType.id, name="PS2").save()

InterfaceTemplate(device_type_id=DeviceType.id, name="iDRAC").save()

InterfaceTemplate = InterfaceTemplate.objects.get(device_type_id=DeviceType.id, name="iDRAC")
InterfaceTemplate.form_factor="1000"
InterfaceTemplate.mgmt_only=True
InterfaceTemplate.save()
