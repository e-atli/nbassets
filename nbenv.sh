#!/bin/bash

echo "Creating Netbox Customer Environment"
echo "===================================="
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo
echo "Using Customer Environment File $1"

if [ -e "$1" ];
  then
  {
    source $1
  }
  else
  {
        echo;
        echo "File $1 not found. Exit.";
        exit
  }
fi

echo
echo "Getting VMware Cluster Information"
echo "=================================="
echo
echo "Following vCenters will be queried:"

NUMVCENTERS=0
while [ ${VCENTER[$NUMVCENTERS]} ]
do
{
  echo "  ${VCENTER[$NUMVCENTERS]}";
  ((NUMVCENTERS++))
}
done

if [ $USER == "" ];
  then
  {
    echo;
    echo -n "Enter Username to connect: ";
    read -s USER
  }
fi

echo
echo -n "Enter Password for User $USER: " 
read -s PASS
echo
echo

for (( i=0; i<$NUMVCENTERS; i++ ))
{
  echo "Connecting to vCenter Server ${VCENTER[$i]}...";
  
  mkdir -p /tmp/nbassets/clusters;
  mkdir -p /tmp/nbassets/virtual_machines;
  
  find /tmp/nbassets/clusters/ -name cl_* | xargs rm
  find /tmp/nbassets/virtual_machines/ -name vm_* | xargs rm
  
  pwsh powershell/read_clusters.ps1 ${VCENTER[$i]} $USER $PASS > /tmp/clusters/cl_${VCENTER[$i]}.py;
  pwsh powershell/read_vms.ps1 ${VCENTER[$i]} $USER $PASS > /tmp/virtual_machines/vm_${VCENTER[$i]}.py
}

find /tmp/nbassets/clusters/ -name cl_* | xargs cat
find /tmp/nbassets/virtual_machines/ -name vm_* | xargs cat

exit 

echo
echo "Searching VM Cluster"
echo "===================="
find clusters -name cl_*
echo
echo "Processing..."
python3 $NETBOX_PATH/manage.py nbshell <python/clusters.py

echo
echo "Done."

echo
echo "Searching Virtual Machines"
echo "=========================="
find virtual_machines -name vm_*
echo
echo "Processing..."
python3 $NETBOX_PATH/manage.py nbshell <python/virtual_machines.py

echo
echo "Done."
