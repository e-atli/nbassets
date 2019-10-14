MFGSLUG = "hpe"
SLUG = "proliant-dl560-gen10"
MODEL = "ProLiant DL560 Gen10"
U_HEIGHT = "2"
IS_FULL_DEPTH = True

POWER_PORT = "PS1"
POWER_PORT = "PS2"

InterfaceTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="iLO").save()

NEW_INTERFACE_TEMPLATE = InterfaceTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="iLO")
NEW_INTERFACE_TEMPLATE.form_factor = "1000"
NEW_INTERFACE_TEMPLATE.mgmt_only = True
NEW_INTERFACE_TEMPLATE.save()
