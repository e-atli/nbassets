import os
import glob

from pathlib import Path

for filename in Path('virtual_machines').glob('**/vm_*'):
    CLUSTER = ''
    NAME = ''
    VCPUS = ''
    MEMORY = ''
    DISK = ''
    ROLE = ''
    STATUS = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            #print(line)
            try:
                exec(line)
            except:
                pass
            if (line.startswith('NAME')) :
                try:
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    NEW_VIRTUAL_MACHINE = VirtualMachine()
                    NEW_VIRTUAL_MACHINE.name = NAME
                    NEW_VIRTUAL_MACHINE.cluster_id = CLUSTERID
                    NEW_VIRTUAL_MACHINE.save()
                except:
                    pass
            if (line.startswith('VCPUS')) :
                try:
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.vcpus = VCPUS
                    VIRTUAL_MACHINE.save()
                except:
                    pass
            if (line.startswith('MEMORY')) :
                try:
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.memory = MEMORY
                    VIRTUAL_MACHINE.save()
                except:
                    pass
            if (line.startswith('DISK')) :
                try:
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.disk = DISK
                    VIRTUAL_MACHINE.save()
                except:
                    pass
            if (line.startswith('ROLE')) :
                try:
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.role = DeviceRole.objects.get(name=ROLE)
                    VIRTUAL_MACHINE.save()
                except:
                    pass
            if (line.startswith('STATUS')) :
                if (STATUS == 'Online') or (STATUS == 'Active') or (STATUS == 'PoweredOn') :
                    STATUS = 1
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.status = STATUS
                    VIRTUAL_MACHINE.save()
                if (STATUS == 'Offline') or (STATUS == 'Inactive') or (STATUS == 'PoweredOff') :
                    STATUS = 0
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.status = STATUS
                    VIRTUAL_MACHINE.save()
                if (STATUS == 'Staged') :
                    STATUS = 3
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.status = STATUS
                    VIRTUAL_MACHINE.save()
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
