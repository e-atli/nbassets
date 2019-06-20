import os
import glob

from pathlib import Path

print("Cluster Types...\n")
for filename in Path('cluster_types').glob('**/ct_*'):
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            if (line.startswith('SLUG')) :
                try:
                    exec(line)
                    ClusterType.objects.get(slug=SLUG).delete()
                except:
                    pass
            line = fp.readline()
    try:
        filename.close
    except:
        pass

print("Device Roles...\n")
for filename in Path('device_roles').glob('**/dr_*'):
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            if (line.startswith('SLUG')) :
                try:
                    exec(line)
                    DeviceRole.objects.get(slug=SLUG).delete()
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
                    DeviceType.objects.get(slug=SLUG).delete()
                except:
                    pass
            line = fp.readline()

for filename in Path('manufacturers').glob('**/mf_*'):
    SLUG = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            if (line.startswith('SLUG')) :
                try:
                    exec(line)
                    Manufacturer.objects.get(slug=SLUG).delete()
                except:
                    pass
            line = fp.readline()

quit()
