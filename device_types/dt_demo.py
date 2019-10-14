# Als MFGSLUG den Slug-Code des gewünschten Herstellers angeben
MFGSLUG = 'demo'

# SLUG ist die ID des Namens.
# - Bindestriche statt Leerzeichen
# - Alles Kleinbuchstaben
# - Der Dateiname richtet sich nach der Slug!
SLUG = 'demo-device-type'

# MODEL ist der ausgeschriebene Name des Assets, der angezeigt wird
MODEL = 'Demo Device Type'

# Anzahl der HEs
U_HEIGHT = '88'

# Volle Bautiefe? True/False
IS_FULL_DEPTH = True

# mit POWER_PORT wird ein Netzteil mit der angegebenen Bezeichnung angelegt.
POWER_PORT = 'Netzteil 1'
POWER_PORT = 'Netzteil 2'

# Um Interfaces anzulegen, zunächst mit IFACE_FF den Port Type angeben.
# 1000 : 1G RJ45 Kupfer Port
# 1100 : 1G SFP Port
# 1200 : 10G SFP+ Port

# dann mit INTERFACE ein reguläres Interface, bzw.
# OOB_MGMT ein Out-Of-Band Management Interface (z.B. iLO, iDRAC).
# IFACE_FF muss nur einmalig für eine Reihe von neuen Interfaces angelegt werden,
# solange sich der Typ nicht ändert.
IFACE_FF = '1000'
OOB_MGMT = '1G RJ45 iDRAC'

INTERFACE = '1G RJ45 Interface'
INTERFACE = '1G RJ45 Interface 2'

IFACE = '1100'
INTERFACE = '1G SFP Interface'

IFACE = '1100'
INTERFACE = '10G SFP+ Interface'
