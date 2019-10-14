MFGSLUG = "hpe"
SLUG = "proliant-dl120-gen9"
MODEL = "ProLiant DL120 Gen9"
U_HEIGHT = "1"
IS_FULL_DEPTH = True

POWER_PORT = "PS1"

InterfaceTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="iLO").save()

NEW_INTERFACE_TEMPLATE = InterfaceTemplate.objects.get(device_type_id=NEW_DEVICE_TYPE.id, name="iLO")
NEW_INTERFACE_TEMPLATE.form_factor = "1000"
NEW_INTERFACE_TEMPLATE.mgmt_only = True
NEW_INTERFACE_TEMPLATE.save()
