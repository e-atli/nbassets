MFGSLUG = 'demo'
SLUG = 'demo-device-type'
MODEL = 'Demo Device Type'
U_HEIGHT = '88'
IS_FULL_DEPTH = True

# mit POWER_PORT wird ein Netzteil mit der angegebenen Bezeichnung angelegt.
POWER_PORT = 'Netzteil 1'
POWER_PORT = 'Netzteil 2'

# Um Interfaces anzulegen, zunächst mit IFACE_FF den Port Type angeben,
# dann mit INTERFACE ein reguläres Interface, bzw.
# OOB_MGMT ein Out-Of-Band Management Interface (z.B. iLO, iDRAC).
# IFACE_FF muss nur einmalig für eine Reihe von neuen Interfaces angelegt werden,
# solange sich der Typ nicht ändert.
IFACE_FF = '1000'
INTERFACE = 'Port 1'
INTERFACE = 'Port 2'

OOB_MGMT = 'iDRAC'
