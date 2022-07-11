#! /bin/bash

if [ $# -ne 1 ]; then
    temps=120
else
    temps=$1
fi

while true; do
    python3 /home/stage/Modeles/miFlora.py >>data.txt
    sleep $temps
done
