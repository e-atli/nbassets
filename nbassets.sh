#!/bin/sh

echo "Creating Netbox Assets"
echo "======================"
echo

export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo

echo "Searching Manufacturers"
echo "======================="
find . -name mf_*.sh
echo

for i in $(find . -name mf_*.sh);
do
  echo "Processing $i..."
  ./$i > /dev/null 2>&1
done

echo
echo "Searching Device Types"
echo "======================"
find . -name dt_*.sh
echo

for i in $(find . -name dt_*.sh);
do
  echo "Processing $i..."
  ./$i > /dev/null 2>&1
done
