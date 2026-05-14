#! /bin/bash
#convert userConfig c files c to csv

BASE_NAME=${1::-2}
echo "new name $BASE_NAME"
SCRATCH_FILE=$BASE_NAME.csv

cp $1 $SCRATCH_FILE
#comment out the first line
sed -i '1 s/^/#/' $SCRATCH_FILE

sed -i 's/SetupReaderForWiegandOnly();/\/\/ Enable Wiegand Only \
	SystemFeatures.OpSettings[HOST_SP_OPTIONS_INDEX] = 0; \
	SystemFeatures.OpSettings[OPERATION_INDEX] \&= ~(OSDP_AUTO_DETECT_ACTIVE); \
	SystemFeatures.OpSettings[EXT_OPERATION_INDEX] \&= ~(TAMPER_INITIATES_OSDP_AUTO); /' $SCRATCH_FILE

sed -i '/fAskHwSupport/c\HW,ASK,ENABLE' $SCRATCH_FILE
sed -i '/i<MAX_CARD_TYPES;/c #i<MAX_CARD_TYPES;' $SCRATCH_FILE
sed -i '/CA_NONE, MAX_CARD_APPS/ cAPP\,ALL,CA_NONE' $SCRATCH_FILE

sed -i 's/\/\//# /' $SCRATCH_FILE
sed -i 's/\]//' $SCRATCH_FILE
sed -i 's/;//' $SCRATCH_FILE
sed -i 's/{//' $SCRATCH_FILE
sed -i 's/}//' $SCRATCH_FILE
sed -i 's/^[ \t]*//;s/[ \t]*$//' $SCRATCH_FILE



sed -i '/^SystemFeatures.mobileConfig.*|=/s/^/MOBILE_AUG,/' $SCRATCH_FILE
sed -i '/^SystemFeatures.mobileConfig.*&=/s/^/MOBILE_MASK,/' $SCRATCH_FILE
sed -i '/^SystemFeatures.mobileConfig.*=/s/^/MOBILE,/' $SCRATCH_FILE


sed -i '/^SystemFeatures.OpSettings.*|=/s/^/OPT_AUG,/' $SCRATCH_FILE


sed -i '/^SystemFeatures.OpSettings.*\&=/s/^/OPT_MASK,/' $SCRATCH_FILE

sed -i '/^SystemFeatures.OpSettings.*=/s/^/OPT,/' $SCRATCH_FILE



sed -i 's/OpSettings\[//' $SCRATCH_FILE


sed -i '/^SystemFeatures.RfProtocols.*/s/^/RF,/' $SCRATCH_FILE
sed -i 's/RfProtocols\[//' $SCRATCH_FILE

sed -i '/^SystemFeatures.CardTypesApps.*/s/^/APP,/' $SCRATCH_FILE
sed -i 's/CardTypesApps\[//' $SCRATCH_FILE


sed -i '/^SystemFeatures.BsFilterMask.*=/s/^/BS_FILTER_MASK, /' $SCRATCH_FILE
sed -i 's/BsFilterMask\[//' $SCRATCH_FILE

sed -i '/^SystemFeatures.BsFilterValue.*=/s/^/BS_FILTER_VALUE, /' $SCRATCH_FILE
sed -i 's/BsFilterValue\[//' $SCRATCH_FILE

sed -i '/^SystemFeatures.Bs.*|=/s/^/BS_AUG, /' $SCRATCH_FILE
sed -i 's/CardTypesApps\[//' $SCRATCH_FILE

sed -i '/^SystemFeatures.Bs.*=/s/^/BS_SET, /' $SCRATCH_FILE

sed -i 's/BsNumBits/NUM_BITS/' $SCRATCH_FILE
sed -i 's/BsAppliedFilter/FILTER/' $SCRATCH_FILE


sed -i 's/|=/,/' $SCRATCH_FILE
sed -i 's/\&=/,/' $SCRATCH_FILE
sed -i 's/=/,/' $SCRATCH_FILE

sed -i 's/SystemFeatures.//' $SCRATCH_FILE
sed -i 's/mobileConfig.//' $SCRATCH_FILE

sed -i 's/\[/,/' $SCRATCH_FILE
sed -i 's/\]//' $SCRATCH_FILE

sed -i 's/| / | wl./' $SCRATCH_FILE

sed -i 's/(uint16_t)//' $SCRATCH_FILE





