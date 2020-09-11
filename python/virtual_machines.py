import os
import glob

from pathlib import Path

for filename in Path('virtual_machines').glob('**/vm_*'):
    CLUSTER = ''
    DISK = ''
    INTERFACE = ''
    MAC_ADDRESS = ''
    MEMORY = ''
    NAME = ''
    ROLE = ''
    STATUS = ''
    VCPUS = ''
    with filename.open() as fp:
        line = fp.readline()
        while line:
            try:
                exec(line)
            except:
                pass
            if (line.startswith('NAME')) :
                print(NAME, sep='', end='...                   \r', flush=True)
                try:
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    try:
                        VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    except:
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
                    STATUS = 'active'
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.status = STATUS
                    VIRTUAL_MACHINE.save()
                if (STATUS == 'Offline') or (STATUS == 'Inactive') or (STATUS == 'PoweredOff') :
                    STATUS = 'offline'
                    CLUSTERID = Cluster.objects.get(name=CLUSTER).id
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VIRTUAL_MACHINE.status = STATUS
                    VIRTUAL_MACHINE.save()
            if (line.startswith('INTERFACE')) :
                try:
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    NEW_VM_INTERFACE = VIRTUAL_MACHINE.interfaces.add()
                    NEW_VM_INTERFACE.name = INTERFACE
                    NEW_VM_INTERFACE.save()
                except:
                    pass
            if (line.startswith('MAC_ADDRESS')) :
                try:
                    VIRTUAL_MACHINE = VirtualMachine.objects.get(cluster=CLUSTERID,name=NAME)
                    VM_INTERFACE = VIRTUAL_MACHINE.interfaces.get(name=INTERFACE)
                    VM_INTERFACE.mac_address = MAC_ADDRESS
                    VM_INTERFACE.save()
                except:
                    pass
            line = fp.readline()
    try:
        filename.close
    except:
        pass

quit()
