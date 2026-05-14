
#! /bin/bash
set -x
PATH_TO_SRC=../../../WallMountReader/src/
USER_KEY_FILE=${PATH_TO_SRC}UserKeys.c
mkdir -p raw
PREFIX=raw/keys_

#remove old files
rm -rf ${PREFIX}*
cat $USER_KEY_FILE
csplit ${USER_KEY_FILE} "/#if OEM_BUILD ==/" {*} -f ${PREFIX}
#revove the first chunk it doesnt' contain any configuration data
rm ${PREFIX}00

sed -i 's/#ifdef //' ${PREFIX}*
sed -i 's/#if OEM_BUILD == //' ${PREFIX}*
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