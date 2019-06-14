#!/bin/sh

echo "Creating Netbox Assets"
echo "======================"
echo

export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"

echo "Searching Manufacturers"
find . -name mf_*.sh

for i in $(find . -name mf_*.sh);
do
  ./$i
done
