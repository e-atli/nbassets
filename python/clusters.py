import os
import glob

from pathlib import Path

for filename in Path('clusters').glob('**/cl_*'):
    TYPE = ''
    NAME = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            print(line)
            try:
                exec(line)
            except:
                pass
            if (line.startswith('NAME')) :
                try:
                    CLUSTER_TYPE = ClusterType.objects.get(name=TYPE)
                    NEW_CLUSTER = Cluster()
                    NEW_CLUSTER.type = CLUSTER_TYPE
                    NEW_CLUSTER.name = NAME
                    NEW_CLUSTER.save()
                except:
                    pass
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
