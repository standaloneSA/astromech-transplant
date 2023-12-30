#!/bin/bash

if [ -z "$2" ] ; then 
    echo "Usage: $0 <agent-name> <serial-port>"
    echo "Where agent-name matches a subdirectory here"
    exit 1
fi

agent=$1
port=$2

# todo: checking
cd $agent
for FILE in * ; do
    for AFILE in ampy -p $port ls
