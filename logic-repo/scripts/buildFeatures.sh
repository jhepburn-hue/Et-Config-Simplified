BASE_PATH=../../src/
FEATURES_FILE=${BASE_PATH}/Features.h
SCRATCH_FILE=features
WLTYPES=standardTypes.py
set -x

grep -hs "#define\|^//" ${BASE_PATH}WlTypes.h ${BASE_PATH}WlGlobals.h ${BASE_PATH}Features.h ${BASE_PATH}Ble.h ${BASE_PATH}Leds.h  ${BASE_PATH}Timers.h  ${BASE_PATH}Wiegand.h \
         ${BASE_PATH}HostInterface.h   ${BASE_PATH}KeyPad.h ${BASE_PATH}NexPacs.h ${BASE_PATH}osdp.h ${BASE_PATH}ScEcpNfc.h \
         ${BASE_PATH}DormaKaba.h \
         ${BASE_PATH}CsnFormat.h ${BASE_PATH}BitStream.h ${BASE_PATH}SymmetricKeys.h ${BASE_PATH}tlv.h ${BASE_PATH}Fips201.h > $SCRATCH_FILE

dos2unix $SCRATCH_FILE
#sed -i ':a; s%(.*)/\*.*\*/%\1%; ta; /\/\*/ !b; N; ba'  $SCRATCH_FILE
sed -i 's/#define //' $SCRATCH_FILE
sed -i 's/false/False/' $SCRATCH_FILE
sed -i 's/true/True/' $SCRATCH_FILE
# ed -i 's/FALSE/False/' $SCRATCH_FILE
# sed -i 's/TRUE/True/' $SCRATCH_FILE
sed -i 's/^[ \t]*//;s/[ \t]*$//' $SCRATCH_FILE
sed -i 's/*H_[ ]*$//;s/*_H[ ]*$//' $SCRATCH_FILE

#remove empty lines
sed -i 's/^$/d' $SCRATCH_FILE
sed -i '/^Binary file/d'  $SCRATCH_FILE
sed -i '/^delayN/d'  $SCRATCH_FILE
sed -i '/(x)/d'  $SCRATCH_FILE
sed -i '/()/d'  $SCRATCH_FILE
sed -i '/^AS3911/d'  $SCRATCH_FILE
sed -i '/ATCA_/d'  $SCRATCH_FILE
sed -i '/BSC_/d'  $SCRATCH_FILE
sed -i '/NOT_ATMEL/d'  $SCRATCH_FILE
sed -i '/ZEPHYR/d'  $SCRATCH_FILE
sed -i '/ATMEL/d'  $SCRATCH_FILE
sed -i '/NOT_ZEPHYR/d'  $SCRATCH_FILE
sed -i '/WIEG_DATA/d' $SCRATCH_FILE
sed -i '/FUTURE_RELEASE/d' $SCRATCH_FILE
sed -i '/RS485_RECEIVE_ENABLE_PIN/d' $SCRATCH_FILE

sed -i '/^ERR_/d'  $SCRATCH_FILE
sed -i '/_H$/d'  $SCRATCH_FILE
sed -i '/H_$/d'  $SCRATCH_FILE
sed -i '/\*  \\/d'  $SCRATCH_FILE
sed -i '/UINT32/d'  $SCRATCH_FILE
sed -i '/\\ *$/d'   $SCRATCH_FILE

#convert comments
sed -i 's/\/\//# /' $SCRATCH_FILE
sed -i 's/\/\*/# /' $SCRATCH_FILE

#add in the = 
sed -i 's/^\(\w\+\s\+\)/\1 = /' $SCRATCH_FILE

#lines ending with an L are evil in python
sed -i 's/ull *$//' $SCRATCH_FILE
sed -i 's/u *$//' $SCRATCH_FILE
sed -i 's/L *$//' $SCRATCH_FILE
sed -i '/NRF_CONFIG_BLOCK/d' $SCRATCH_FILE
sed -i '/NRF_CAP_GET/d' $SCRATCH_FILE

sed -i 's/(\w*int.*_t)//' $SCRATCH_FILE
sed -i 's/(void\*)//' $SCRATCH_FILE


mv $SCRATCH_FILE $SCRATCH_FILE.py
