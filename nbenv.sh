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

NBASSETSPATH=$PWD
PREFIX="/tmp/nbassets"

for (( i=0; i<$NUMVCENTERS; i++ ))
{
  echo "Connecting to vCenter Server ${VCENTER[$i]}...";
  
  mkdir -p $PREFIX/clusters;
  mkdir -p $PREFIX/virtual_machines;
  
  find $PREFIX/clusters/ -name cl_* | xargs rm
  find $PREFIX/virtual_machines/ -name vm_* | xargs rm
  
  echo "  Saving Cluster information to $PREFIX/clusters/cl_${VCENTER[$i]}.py"
  pwsh powershell/read_clusters.ps1 ${VCENTER[$i]} $USER $PASS > $PREFIX/clusters/cl_${VCENTER[$i]}.py;
  echo "  Saving Virtual Machine information to $PREFIX/virtual_machines/vm_${VCENTER[$i]}.py"
  pwsh powershell/read_vms.ps1 ${VCENTER[$i]} $USER $PASS > $PREFIX/virtual_machines/vm_${VCENTER[$i]}.py
}

find $PREFIX/clusters/ -name cl_* | xargs cat
find $PREFIX/virtual_machines/ -name vm_* | xargs cat

cd $PREFIX

echo
echo "Searching VM Cluster"
echo "===================="
find clusters -name cl_*
echo
echo "Processing..."
python3 $NETBOX_PATH/manage.py nbshell <$NBASSETSPATH/python/clusters.py

echo
echo "Done."

echo
echo "Searching Virtual Machines"
echo "=========================="
find virtual_machines -name vm_*
echo
echo "Processing..."
python3 $NETBOX_PATH/manage.py nbshell <$NBASSETSPATH/python/virtual_machines.py

echo
echo "Done."
