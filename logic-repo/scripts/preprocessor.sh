#!/bin/bash

BASE_PATH=../WallMountReader/WallMountReader/src/

SCRATCH_FILE=prefeatures


gcc -dMM -include ${BASE_PATH}Features.h -include ${BASE_PATH}Ble.h </dev/null >${SCRATCH_FILE}
sed -i 's/#define //' $SCRATCH_FILE

sed -i '/^__\w*/d'  $SCRATCH_FILE

#add in the = 
sed -i 's/^\(\w\+\s\+\)/\1 = /' $SCRATCH_FILE