MFGSLUG = "hpe"
SLUG = "proliant-dl580-gen8"
MODEL = "ProLiant DL580 Gen8"
U_HEIGHT = "4"
IS_FULL_DEPTH = True

POWER_PORT = "PS1"
POWER_PORT = "PS2"

InterfaceTemplate(device_type_id=NEW_DEVICE_TYPE.id, name="iLO").save()

# Um Interfaces anzulegen, zunächst mit IFACE_FF den Port Type angeben,
# dann mit INTERFACE ein reguläres Interface, bzw.
# OOB_MGMT ein Out-Of-Band Management Interface (z.B. iLO, iDRAC).
# IFACE_FF muss nur einmalig für eine Reihe von neuen Interfaces angelegt werden,
# solange sich der Typ nicht ändert.
IFACE_FF = '1000'
OOB_MGMT = 'iLO'
