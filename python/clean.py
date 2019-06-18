import os
import glob

from pathlib import Path

for filename in Path('device_roles').glob('**/dr_*'):
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            try:
                exec(line)
            except:
                pass
            if (line.startswith('SLUG')) :
                try:
                    DeviceRole(slug=SLUG).delete()
                except:
                    pass
                NEW_DEVICE_ROLE = DeviceRole.objects.get(slug=SLUG)
            line = fp.readline()
    try:
        filename.close
    except:
        pass

for filename in Path('device_types').glob('**/dt_*'):
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            try:
                exec(line)
            except:
                pass
            if (line.startswith('SLUG')) :
                try:
                    DeviceType(slug=SLUG).delete()
                except:
                    pass

quit()
