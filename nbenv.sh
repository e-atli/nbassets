#!/bin/bash

# This script gets all clusters and virtual Machines
# from VMware vCenter Server and puts them into Netbox.

# 2020-09-11 Update script to use VENV

echo "Creating Netbox Customer Environment"
echo "===================================="
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo
echo "Using Customer Environment File $1"

# Check, if given environment file really exists. If not, exit.
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

# Get number of vCenter Servers to connect to.
# Environment file needs to be specified like this:
# VCENTER[0]='https://vcenter-url01.fqdn.local'
# VCENTER[1]='https://vcenter-url02.fqdn.local'
# VCENTER[2]=...
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

# If environment file doesn't contain CREDFILE variable
# ask for proper CREDFILE via CLI
if [ $CREDFILE == "" ];
  then
  {
    echo;
    echo -n "Enter Credential File (See How-To.txt): ";
    read -s CREDFILE
  }
fi

# Check if CREDFILE really exists. If not, exit the script.
if [ -n $CREDFILE];
  then
    {
      echo "File $CREDFILE not found. Exit.";
      exit
    }
fi

# Set NBASSETSPATH to the current folder, assuming it is run directly
NBASSETSPATH=$PWD

# Set PREFIX for temporary stored inventory data
PREFIX="/tmp/nbassets"

# Check if subfolders for clusters and virtual machines exists
# from an previous inventory
if [ -d $PREFIX/clusters ];
  then
    rm -fr $PREFIX/clusters;
fi

if [ -d $PREFIX/virtual_machines ];
  then
    rm -fr $PREFIX/virtual_machines;
fi

# Create subfolders for inventory
mkdir -p $PREFIX/clusters
mkdir -p $PREFIX/virtual_machines

# For each vCenter specified, call powershell with the inventory script
for (( i=0; i<$NUMVCENTERS; i++ ))
{
  echo "Connecting to vCenter Server ${VCENTER[$i]}...";
  echo "Saving Cluster and Virtual Machine information to PATH: $PREFIX"
  time pwsh powershell/get-vsphere.ps1 ${VCENTER[$i]} $CREDFILE $PREFIX
}

cd $PREFIX

# Before running nbshell, enter venv
if [ -e "$NETBOX_PATH/../venv/bin/activate" ];
  then
    {
      echo
      echo "VENV binary detected. Entering VENV..."
      source $NETBOX_PATH/../venv/bin/activate
    }
  else
    {
      echo
      echo "Not using venv."
    }
fi

# Write cluster inventory into Netbox
echo
echo "Searching VMware Cluster"
echo "========================"
find clusters -name cl_*
echo
echo "Processing..."
python3 $NETBOX_PATH/manage.py nbshell <$NBASSETSPATH/python/clusters.py
echo
echo "Done."

# Write cluster inventory into Netbox
echo
echo "Searching Virtual Machines"
echo "=========================="
find virtual_machines -name vm_*
echo
echo "Processing..."
python3 $NETBOX_PATH/manage.py nbshell <$NBASSETSPATH/python/virtual_machines.py
echo
echo "Done."

# Exit VENV
if [ $VIRTUAL_ENV != '' ];
  then
    echo "Leaving VENV..."
    deactivate;
fi
