MFGSLUG = "dell-emc"
SLUG = "poweredge-t420"
MODEL = "PowerEdge T420"
U_HEIGHT = "4"
IS_FULL_DEPTH = True

POWER_PORT = "PS1"
POWER_PORT = "PS2"

InterfaceTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="iDRAC").save()

NEW_INTERFACE_TEMPLATE = InterfaceTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="iDRAC")
NEW_INTERFACE_TEMPLATE.form_factor="1000"
NEW_INTERFACE_TEMPLATE.mgmt_only=True
NEW_INTERFACE_TEMPLATE.save()