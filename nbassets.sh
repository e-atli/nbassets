#!/bin/bash

echo "Creating Netbox Assets"
echo "======================"
export NETBOX_PATH="/opt/netbox/netbox"
echo "Netbox Path: $NETBOX_PATH"
echo

echo "Searching Manufacturers"
echo "======================="
find . -name mf_*
echo

for i in $(find . -name mf_*);
do
  echo "Processing $i..."
  source $i > /dev/null 2>&1
done

echo
echo "Searching Device Types"
echo "======================"
find . -name dt_*
echo

for i in $(find . -name dt_*);
do
  echo "Processing $i..."
  source $i > /dev/null 2>&1
done
