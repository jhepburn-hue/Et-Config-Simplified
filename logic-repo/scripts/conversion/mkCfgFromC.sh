
#! /bin/bash

PATH_TO_SRC=../../../WallMountReader/src/
USER_CONFIG_FILE=${PATH_TO_SRC}UserConfig.c
mkdir -p raw
PREFIX=raw/config_

#remove old files
rm -rf ${PREFIX}*

csplit ${USER_CONFIG_FILE} /#if.*==/ {*} -f ${PREFIX}

#revove the first chunk it doesnt' contain any configuration data
rm ${PREFIX}00

sed -i 's/#if.*== //' ${PREFIX}*
sed -i 's/#endif//'  ${PREFIX}*
sed -i 's/}//' ${PREFIX}*
sed -i 's/ *$//g' ${PREFIX}*

#!/bin/sh
for f in ${PREFIX}*; do
#    d="$(head -n 1 "$f" | awk '{print CFG_$1}')"

    d="$(head -n 1 "$f" | awk '{print $1}')"
    newfile=${PREFIX}${d}
    # remove leading whitespace characters
    newfile="${newfile#"${newfile%%[![:space:]]*}"}"
    # remove trailing whitespace characters
    newfile="${newfile%"${newfile##*[![:space:]]}"}"
    echo $newfile
    if [ ! -f "$newfile" ]; then
        mv "$f" $newfile.c
    else
        echo "File '$newfile' already exists! Skiped '$f'"
    fi
done