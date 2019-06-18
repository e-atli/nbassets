import os
import glob

from pathlib import Path

for filename in Path('device_roles').glob('**/dr_*'):
    COLOR = ''
    NAME = ''
    NEW_DEVICE_ROLE = ''
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            #print(line)
            try:
                exec(line)
            except:
                pass
            if (line.startswith('SLUG')) :
                try:
                    DeviceRole(slug=SLUG).save()
                except:
                    pass
                NEW_DEVICE_ROLE = DeviceRole.objects.get(slug=SLUG)
            if (line.startswith('COLOR')) :
                NEW_DEVICE_ROLE.color = COLOR
                NEW_DEVICE_ROLE.save()
            if (line.startswith('NAME')) :
                NEW_DEVICE_ROLE.name = NAME
                NEW_DEVICE_ROLE.save()
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
