#!/bin/bash

START=9000
COUNT=20

echo "Starting $COUNT nodes..."

for ((i=0;i<COUNT;i++))
do
PORT=$((START+i))

python nodes/node_server.py $PORT > /dev/null 2>&1 &

sleep 0.05

done

echo "Cluster started"
