#! /bin/bash

#attempt to convert all files with a given prefix to CSV files...

PREFIX=raw/config_

./mkCfgFromC.sh

for f in ${PREFIX}*; do
    ./cfgToCsv.sh $f
done