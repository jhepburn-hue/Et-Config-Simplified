echo "usage $0 Sales_CSV_file "
echo "this script automates the building of a configuration based off of a sales sheet"


SALES_CSV=$1
#CFG_NAME=$2
OUT_NAME=$(grep -w "Config Name" $SALES_CSV |awk -F "," '{print $2}'  )
# | grep -w "Config Name")
#  |awk -F \",\" '{print $2}')
echo "OUT name is" $OUT_NAME

if [ -z "$1" ];then
	echo "missing sales sheet path"
	exit 2
fi

if [ "$SALES_CSV" == "$OUT_NAME.csv" ];then
	echo "input and output files match Aborting. "
	echo "The output file is built off of the config Name in the provided CSV input"
	exit 4
fi

CONFIG_DIR="../configs/nonApproved/WS"
if ! python3 salesToCfg.py $SALES_CSV ; then
	echo please inspect configs
	exit 1
fi
echo "finished converting sales sheet"
git add configMap.txt
mkdir -p $CONFIG_DIR
python3 ../scripts/buildCfg.py $OUT_NAME.csv