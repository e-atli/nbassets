import os
import glob

from pathlib import Path

for filename in Path('device_types').glob('**/dt_*'):
    IS_FULL_DEPTH = False
    MANUFACTURER_ID = ''
    MFGSLUG = ''
    NEW_DEVICE_TYPE = ''
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
            if (line.startswith('MFGSLUG')) :
                MANUFACTURER_ID = Manufacturer.objects.get(slug=MFGSLUG).id
            if (line.startswith('SLUG')) :
                try:
                    DeviceType(slug=SLUG, manufacturer_id=MANUFACTURER_ID).save()
                except:
                    pass
                NEW_DEVICE_TYPE = DeviceType.objects.get(slug=SLUG)
            if (line.startswith('MODEL')) :
                NEW_DEVICE_TYPE.model = MODEL
                NEW_DEVICE_TYPE.save()
            if (line.startswith('U_HEIGHT')) :
                NEW_DEVICE_TYPE.u_height = U_HEIGHT
                NEW_DEVICE_TYPE.save()
            if (line.startswith('IS_FULL_DEPTH')) :
                NEW_DEVICE_TYPE.is_full_depth = True
                NEW_DEVICE_TYPE.save()
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
