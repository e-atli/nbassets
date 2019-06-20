import os
import glob

from pathlib import Path

for filename in Path('cluster_types').glob('**/ct_*'):
    NAME = ''
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
                    ClusterType(slug=SLUG).save()
                except:
                    pass
                NEW_CLUSTER_TYPE = ClusterType.objects.get(slug=SLUG)
            if (line.startswith('NAME')) :
                NEW_CLUSTER_TYPE.name = NAME
                NEW_CLUSTER_TYPE.save()
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
