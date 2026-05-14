
today=`date +%b-%d`
PUBLISH_PATH="/media/NAS/TestReleases/WsConfigs/$today$1"
SRC_PATH="../configs/nonApproved/WS"


for configFile in $SRC_PATH/*.bin; do
    CONFIG_NAME=$(echo ${configFile##*/} | cut -d'_' -f1)
    STD_PATH=$PUBLISH_PATH/standard/$CONFIG_NAME
    PROD_PATH=$PUBLISH_PATH/production/$CONFIG_NAME
    mkdir -p $PROD_PATH
    mkdir -p $STD_PATH
    echo $configFile to $STD_PATH
    cp $configFile $STD_PATH
    mv $STD_PATH/*PT.bin $PROD_PATH
    
done
