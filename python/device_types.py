import os
import glob

from pathlib import Path

for filename in Path('device_types').glob('**/dt_*'):
    IFACE_FF = ''
    INTERFACE = ''
    IS_FULL_DEPTH = False
    MANUFACTURER_ID = ''
    MFGSLUG = ''
    MODEL = ''
    NEW_DEVICE_TYPE = ''
    OOB_MGMT = ''
    POWER_OUTLET = ''
    POWER_PORT = ''
    R_F_PORT = ''
    R_F_TYPE = ''
    SLUG = ''
    U_HEIGHT = '1'
    with filename.open() as fp:
        line = fp.readline()
        while line:
            #print(line)
            try:
                exec(line)
            except:
                pass
            if (line.startswith('INTERFACE')) :
                try:
                    NEW_INTERFACE_TEMPLATE = InterfaceTemplate()
                    NEW_INTERFACE_TEMPLATE.device_type_id = NEW_DEVICE_TYPE.id
                    NEW_INTERFACE_TEMPLATE.name = INTERFACE
                    NEW_INTERFACE_TEMPLATE.form_factor = IFACE_FF
                    NEW_INTERFACE_TEMPLATE.save()
                except:
                    pass
            if (line.startswith('OOB_MGMT')) :
                try:
                    NEW_INTERFACE_TEMPLATE = InterfaceTemplate()
                    NEW_INTERFACE_TEMPLATE.device_type_id = NEW_DEVICE_TYPE.id
                    NEW_INTERFACE_TEMPLATE.name = OOB_MGMT
                    NEW_INTERFACE_TEMPLATE.form_factor = IFACE_FF
                    NEW_INTERFACE_TEMPLATE.mgmt_only = True
                    NEW_INTERFACE_TEMPLATE.save()
                except:
                    pass
            if (line.startswith('IS_FULL_DEPTH')) :
                NEW_DEVICE_TYPE.is_full_depth = IS_FULL_DEPTH
                NEW_DEVICE_TYPE.save()
            if (line.startswith('MFGSLUG')) :
                MANUFACTURER_ID = Manufacturer.objects.get(slug=MFGSLUG).id
            if (line.startswith('MODEL')) :
                NEW_DEVICE_TYPE.model = MODEL
                NEW_DEVICE_TYPE.save()
            if (line.startswith('PART_NUMBER')):
                NEW_DEVICE_TYPE.part_number = PART_NUMBER
                NEW_DEVICE_TYPE.save()
            if (line.startswith('POWER_OUTLET')) :
                try:
                    PowerOutletTemplate(device_type_id=NEW_DEVICE_TYPE.id, name=POWER_OUTLET).save()
                except:
                    pass
            if (line.startswith('POWER_PORT')) :
                try:
                    PowerPortTemplate(device_type_id=NEW_DEVICE_TYPE.id, name=POWER_PORT).save()
                except:
                    pass
            if (line.startswith('R_F_PORT')) :
                try:
                    NEW_REAR_PORT_TEMPLATE = RearPortTemplate()
                    NEW_REAR_PORT_TEMPLATE.device_type_id = NEW_DEVICE_TYPE.id
                    NEW_REAR_PORT_TEMPLATE.name = R_F_PORT
                    NEW_REAR_PORT_TEMPLATE.positions = '1'
                    NEW_REAR_PORT_TEMPLATE.type = R_F_TYPE
                    NEW_REAR_PORT_TEMPLATE.save()
                    NEW_FRONT_PORT_TEMPLATE = FrontPortTemplate()
                    NEW_FRONT_PORT_TEMPLATE.device_type_id = NEW_DEVICE_TYPE.id
                    NEW_FRONT_PORT_TEMPLATE.name = R_F_PORT
                    NEW_FRONT_PORT_TEMPLATE.rear_port_id = NEW_REAR_PORT_TEMPLATE.id
                    NEW_FRONT_PORT_TEMPLATE.rear_port_position = '1'
                    NEW_FRONT_PORT_TEMPLATE.type = R_F_TYPE
                    NEW_FRONT_PORT_TEMPLATE.save()
                except:
                    pass
            if (line.startswith('SLUG')) :
                try:
                    DeviceType(slug=SLUG, manufacturer_id=MANUFACTURER_ID).save()
                except:
                    pass
                NEW_DEVICE_TYPE = DeviceType.objects.get(slug=SLUG)
            if (line.startswith('U_HEIGHT')) :
                NEW_DEVICE_TYPE.u_height = U_HEIGHT
                NEW_DEVICE_TYPE.save()
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
