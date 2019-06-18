import os
import glob

from pathlib import Path

for filename in Path('device_roles').glob('**/dr_*'):
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            if (line.startswith('SLUG')) :
                try:
                    exec(line)
                    DeviceRole(slug=SLUG).delete()
                except:
                    pass
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
            if (line.startswith('SLUG')) :
                try:
                    exec(line)
                    DeviceType(slug=SLUG).delete()
                except:
                    pass

quit()
