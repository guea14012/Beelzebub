#!/bin/bash

START=9000
COUNT=20

for ((i=0;i<COUNT;i++))
do
PORT=$((START+i))

STATUS=$(curl -s http://127.0.0.1:$PORT/health)

echo "Node $PORT -> $STATUS"

done
