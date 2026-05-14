#! /bin/bash
# build the configutation after the bin has been built.


#Extract the #defines first
./buildFeatures.sh
mkdir -p ../configs/nonApproved/WS
for configFile in ../CSV/WS/*.csv; do
    echo $configFile
    python3 ./buildCfg.py $configFile
    if [ $? -ne 0 ];then
        echo "error converting $configFile"
        exit 2
    fi

done
#now update anything that is used for bin file creation
ls ../configs/Approved/WS | xargs -I % cp ../configs/nonApproved/WS/% ../configs/Approved

