MFGSLUG = "dell-emc"
SLUG = "poweredge-r520"
MODEL = "PowerEdge R520"
U_HEIGHT = "2"
IS_FULL_DEPTH = True

PowerPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="PS1").save()
PowerPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="PS2").save()

InterfaceTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="iDRAC").save()

NEW_INTERFACE_TEMPLATE = InterfaceTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="iDRAC")
NEW_INTERFACE_TEMPLATE.form_factor = "1000"
NEW_INTERFACE_TEMPLATE.mgmt_only = True
NEW_INTERFACE_TEMPLATE.save()
