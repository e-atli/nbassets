MFGSLUG = "dell-emc"
SLUG = "poweredge-r220"
MODEL = "PowerEdge R220"
U_HEIGHT = "1"
FULL_HEIGHT = True

PowerPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="PS1").save()
PowerPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="PS2").save()

InterfaceTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="iDRAC").save()

NEW_INTERFACE_TEMPLATE = InterfaceTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="iDRAC")
NEW_INTERFACE_TEMPLATE.form_factor = "1000"
NEW_INTERFACE_TEMPLATE.mgmt_only = True
NEW_INTERFACE_TEMPLATE.save()
