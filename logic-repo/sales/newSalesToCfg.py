import csv
from os import error
import sys
import warnings
import os.path
from os import path

leafCCApp = "None"
leafSiApp = "None"
csnFormat= "Standard"
buildIndex = 0
extraBuildIndex = 0
sales_file = sys.argv[1]

manualReview = False
FM = False
WS = False

# added in wallet config
def ledColorToFirmwareId(color):
    switch = {
        "off": "BLACK_LED",
        "red": "RED_LED",
        "green": "GREEN_LED",
        "amber": "RED_GREEN_LEDS",
        "blue": "BLUE_LED",
        "magenta": "RED_BLUE_LEDS",
        "cyan": 'GREEN_BLUE_LEDS',
        "white": 'RED_GREEN_BLUE_LEDS'
        # this is also defined but doesn't really apply for config settings ALT_RED_GREEN_LEDS    8
    }
    return switch.get(color.lower(), "BAD COLOR")


def onToBool(name):
    if "on" == name.lower():
        return True
    return False


def cfgWrite(file, value):
    file.write(value)
    file.write("\n")
    # print(value)


def manualReviewMsg():
    print(" print config generated but needs manual review")
    warnings.warn("config generated but needs manual review")


def decomment(csvfile):
    for row in csvfile:
        raw = row.split('#')[0].strip()
        if raw:
            yield raw

mobileTCI = 0
if (False == path.exists(sales_file)):
    print ("unable to find file ", sales_file)
    exit (1)

# print("attempting to open ", sys.argv[1])
with open(sales_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    options = list(line for line in reader if line)

for setting in options:
    if setting[0] == 'Config Name':
        outFileName = setting[1]
    if setting[0] == 'Config ID':
        if int(setting[1]) > 255:
            temp1 = int(setting[1])
            temp = hex(temp1)[2:].zfill(4)
            extraBuildIndex = int(temp[:2],16) * 256
            print(extraBuildIndex)
            buildIndex = int(temp[2:4],16)
            print(buildIndex)
        else:
            buildIndex = setting[1]
    elif (setting[0][2:]) == "WS":
        for index in range(3):
            if "y" == setting[index][0].lower():
                WS = True
    elif (setting[0][2:]) == "FM":
        for index in range(3):
            if "y" == setting[index][0].lower():
                FM = True
    elif setting[0] == 'Idle LED':
        idleLed = ledColorToFirmwareId(setting[2])
    elif setting[0] == 'Credential Report LED':
        credLed = ledColorToFirmwareId(setting[2])
    elif setting[0] == 'Beeper':
        beeper = onToBool(setting[2])
    elif setting[0] == 'Keypad Format':
        kpFormat = setting[2].lower()
    elif setting[0] == 'Tamper Monitoring':
        tamper = onToBool(setting[2])
    elif setting[0] == "Casi Output Format":
        outFormat = setting[2]
    elif setting[0] == "Supervision State":
        supervisionState = setting[2]
    elif setting[0].startswith('Leaf Si'):
        leafSiApp = setting[2].lower()
    elif setting[0] == 'Leaf Cc Application (Kc1)':
        leafCCApp = setting[2].lower()
    elif setting[0].startswith('Keyset ID'):
        leafId = setting[2]        
    elif setting[0] == 'Other Custom HF Application':
        hfApp = setting[2].lower()
        if 'none' != hfApp:
            manualReview = True
    elif setting[0] == 'CustomApplicationNotes':
        hfNotes = setting[2]
        # manualReview = True
    elif setting[0] == 'MFC CSN':
        mfcCsn = onToBool(setting[2])
        mfcCsnFormat= setting[3]
    elif setting[0] == 'EV1/EV2 CSN':
        ev1Csn = onToBool(setting[2])
        ev1CsnFormat= setting[3]
    elif setting[0] == 'iClass CSN':
        iClassCsn = onToBool(setting[2])
        iClassCsnFormat= setting[3]
    elif setting[0] == 'ISO15693 CSN':
        ISO15693Csn = onToBool(setting[2])
        ISO15693CsnFormat= setting[3]
    elif setting[0] == 'ISO14443A CSN':
        ISO14443A = onToBool(setting[2])
        ISO14443ACsnFormat= setting[3]
    elif setting[0] == 'FSK Prox':
        fsk = onToBool(setting[2])
    elif setting[0] == 'ASK Prox':
        ask = onToBool(setting[2])
    elif setting[0] == 'Prox Filter':
        proxFilter = onToBool(setting[2])
        if proxFilter:
            manualReview = True
    elif setting[0] == 'ProxFilterDescription':
        proxFilterDesc = setting[2]
        # manualReview = True
    elif setting[0] == 'BLE Advertising Config':
        bleAdv = setting[2]
    elif setting[0] == 'BLE Functionality':
        bleFunc = setting[2]
    elif setting[0] == 'NFC Functionality':
        nfc = setting[2]
    elif setting[0] == 'Mobile Keyset':
        mobileKey = setting[2]
    elif setting[0] == 'Legacy Credentials (Sym Blue, Brivo)':
        bleLegacy = onToBool(setting[2])
    elif setting[0] == 'Transport Mode':
        mobileTrans = setting[2]
    elif setting[0] == 'ECP DESFire':
        mobileDESFire = setting[2]
    elif setting[0] == 'ECP TCI':
        if setting[2]:
            mobileTCI = str(setting[2])
            manualReview = True
    elif setting[0] == 'Apple Meridian Bit Count':
        meridianbitcount = int(setting[2])
    elif setting[0] == 'MiFare2Go':
        Mifare2Go = setting[2]
    




if FM:
    # warnings.warn("not yet supported by this tool")
    # sys.exit(2)
    pass

if WS:
    # print("building  ws configuration")
    pass

configId = outFileName.split('-')[0]

# inCfg = csv.DictReader(open("configMap.txt"))
# usedIds = []
# idFound = False
# for row in inCfg:
#     usedIds.append((row["ID"],0))
#     if row["NAME"] == configId:
#         buildIndex = row["ID"]
#         idFound = True
# if False == idFound:
#     for testId in range (255):
#         if  testId not in usedIds:
#             buildIndex = hex(testId)
#             with open("configMap.txt","a") as file_object:
#                 file_object.write(f"\n{configId},{buildIndex}")
#             break

if manualReview:
    manualReviewMsg()

outFile = open(outFileName + ".csv", 'w')
rfIndex = 0
mfcIndex = 0
cfgWrite(outFile, f"#autogenerated configuration {outFileName}\n")
cfgWrite(outFile, '#Default keys')
cfgWrite(outFile, 'FEATURE_MANAGEMENT_READ_KEYSET, ETHOS:FEATURE_READ')
cfgWrite(outFile, 'FEATURE_MANAGEMENT_WRITE_KEYSET, ETHOS:FEATURE_WRITE')

# cfgWrite(outFile, 'USER_APP_OCPSK_KEYSET,ETHOS:USER_APP_CARD_MASTER')
# cfgWrite(outFile, 'USER_APP_READ_KEYSET,ETHOS:USER_APP_CARD_WRITE')
#
# cfgWrite(outFile, 'USER_APP_CARD_MASTER_KEYSET , ETHOS:USER_APP_CARD_MASTER')
# cfgWrite(outFile, 'USER_APP_CARD_WRITE_KEYSET , ETHOS:USER_APP_CARD_WRITE')
cfgWrite(outFile, 'EXT_MEM_KEYSET , ETHOS:EXT_MEM')
cfgWrite(outFile, 'BLE_KEYSET , ETHOS:BLE')
cfgWrite(outFile, 'MFC_KEYSET , ETHOS:MFC')
# cfgWrite(outFile, 'USER_APP2_K1_KEYSET , ETHOS:USER_APP2_K1')
# cfgWrite(outFile, 'USER_APP2_K2_KEYSET , ETHOS:USER_APP2_K2')
#
# cfgWrite(outFile, 'LEAF_IP_OCPSK_KEYSET , Lk00001:Ksi')
# cfgWrite(outFile, 'LEAF_IP_READ_KEYSET ,Lk00001:Kv1')
#
# cfgWrite(outFile, 'LEAF_KHSENC1_KEYS , ETHOS:LEAF_KHSENC1')
# cfgWrite(outFile, 'LEAF_KHSENC2_KEYS , ETHOS:LEAF_KHSENC2')
# cfgWrite(outFile, 'LEAF_HSREAD_KEYS , ETHOS:LEAF_HSREAD')
# cfgWrite(outFile, 'LEAF_KBLEENC2_KEYS , ETHOS:LEAF_KBLEENC2')


cfgWrite(outFile, f"OPT_AUG,BUILD_INDEX , {buildIndex}")
if extraBuildIndex != 0:
    cfgWrite(outFile, f"EXT_BUILD_INDEX , {extraBuildIndex}")
cfgWrite(outFile, "\n")
cfgWrite(outFile, "#STEP2: AV and Output formats")
if WS:
    cfgWrite(outFile, "OPT_AUG, WIEGAND_DATA_OPTIONS_INDEX, WIEGAND_CASI_4001_2_MASK")

if FM:
   if outFormat == "CASI_4002":
       pass
# Leaving for when F2F config needs to be supported
# if "CASI_4002" == outFormat:
# elif "CASI_4001"

cfgWrite(outFile, f"LED, DEFAULT_LED_PWM_DUTY_CYCLES, {idleLed} , {credLed}")
if not beeper:
    cfgWrite(outFile, "#Custom beep time of 0 seconds, so really, no beep on card read.")
    cfgWrite(outFile, "	OPT_AUG, CARD_AV_OPTIONS_1_INDEX, CARD_AV_BEEPER_ENABLED;")

cfgWrite(outFile,"#  Enable Host Controlled AV" )
cfgWrite(outFile, "OPT_AUG,OPERATION_INDEX , ENABLE_HOST_CNTL_AV")


cfgWrite(outFile, "#  Setup the default key pad map to the specified format with LEDs back lights always on,")
cfgWrite(outFile, "#  and beep with each key press.")
if '8-bit' == kpFormat:
    # cfgWrite(outFile,
    #          "OPT,KEYPAD_OPTIONS_INDEX,(KP_FORMAT_8_BIT  | wl.KEYPAD_BEEP_ACTIVE_MASK | wl.KEYPAD_LED_IDLE_MASK | "
    #          "wl.KEYPAD_LED_ACTIVE_MASK)")
    #this is the default we don't need to do anything
    pass
elif '4-bit' == kpFormat:
    cfgWrite(outFile,
             "OPT,KEYPAD_OPTIONS_INDEX,(KP_FORMAT_4_BIT  | wl.KEYPAD_BEEP_ACTIVE_MASK | wl.KEYPAD_LED_IDLE_MASK | "
             "wl.KEYPAD_LED_ACTIVE_MASK | wl.KEYPAD_LED_INVERT_MASK)")
elif 'buffered 26-bit' == kpFormat:
    cfgWrite(outFile,
             "OPT,KEYPAD_OPTIONS_INDEX,(KP_FORMAT_26_BIT  | wl.KEYPAD_BEEP_ACTIVE_MASK | wl.KEYPAD_LED_IDLE_MASK | "
             "wl.KEYPAD_LED_ACTIVE_MASK)")

# # this is only used form AMAG configuations
# cfgWrite(outFile,
#          "OPT,OSDP_KP_OPTIONS_INDEX,(KP_FORMAT_ASCII | wl.KEYPAD_BEEP_ACTIVE_MASK | wl.KEYPAD_LED_IDLE_MASK | "
#          "wl.KEYPAD_LED_ACTIVE_MASK)")

if tamper:
    cfgWrite(outFile, "#  Tamper Signal Line Enabled")
    cfgWrite(outFile, "OPT_AUG, OPERATION_INDEX , ENABLE_TAMPER_CNTRL_LINE")

###############################################################################
cfgWrite(outFile, "\n")
cfgWrite(outFile, "#STEP 3: HF")
leaf = False
leafSI = False

if "leaf cc" == leafCCApp.lower():
    # for word in hfNotes:
    #     if (word.startswith("lk")) or (word.startswith("Lk")) or (word.startswith("LK")) :
    #         keyset = word
    leaf = True

    if leafId is not None:
        cfgWrite(outFile,  "OPT,LEAF_IP_DEF_INDEX , 40")
        cfgWrite(outFile, f"LEAF_IP_OCPSK_KEYSET, {leafId}:Kc1")
        cfgWrite(outFile, f"LEAF_IP_READ_KEYSET,  {leafId}:Kc1")
        if 'Enabled'== mobileDESFire:
            cfgWrite(outFile, "OPT,LEAF_IP_KS1_INDEX , LEAF_IP_IGNORE_KEYSET_MASK")
            cfgWrite(outFile, "OPT,LEAF_IP_KS2_INDEX , LEAF_IP_IGNORE_KEYSET_MASK")
            cfgWrite(outFile, "OPT,LEAF_IP_KS3_INDEX , LEAF_IP_IGNORE_KEYSET_MASK")
    else:
        # failed to infer lk number for custom flag harass the user
        warnings.warn("expected to find Custom keyset number")
        manualReview = True
    #check for OEM configuration
    if "leaf si" == leafSiApp.lower():
        cfgWrite(outFile, "LEAF_IP_KS1_OCPSK_KEYSET, Lk00001:Ksi")
        cfgWrite(outFile, "LEAF_IP_KS1_READ_KEYSET, Lk00001:Kv1")
        cfgWrite(outFile,  "OPT,LEAF_IP_KS1_INDEX , 1")
        cfgWrite(outFile, "LEAF_IP_KS3_OCPSK_KEYSET, Lk70003:Kr12")
        cfgWrite(outFile, "LEAF_IP_KS3_READ_KEYSET, Lk70003:Kr13")
        leafSI = True
elif "leaf si" == leafSiApp.lower():
    cfgWrite(outFile,  "OPT,LEAF_IP_DEF_INDEX , 1")
    cfgWrite(outFile, "LEAF_IP_OCPSK_KEYSET, Lk00001:Ksi")
    cfgWrite(outFile, "LEAF_IP_READ_KEYSET, Lk00001:Kv1")
    cfgWrite(outFile, "LEAF_IP_KS3_OCPSK_KEYSET, Lk70003:Kr12")
    cfgWrite(outFile, "LEAF_IP_KS3_READ_KEYSET, Lk70003:Kr13")
    leaf = True
    leafSI = True

######################################################################
cfgWrite(outFile, "\n")
cfgWrite(outFile, "#STEP 4: CSN")

B_DEFAULT_CSN = False

if ISO14443A and ISO15693Csn and iClassCsn and mfcCsn and ev1Csn:
    B_DEFAULT_CSN = True
else:
    cfgWrite(outFile, 'APP,ALL , CA_NONE')

rfIndex = 0
mfcIndex =0

if not B_DEFAULT_CSN:
    if ISO14443A:
        cfgWrite(outFile, f"APP,CT_ISO_14443A_3, {mfcIndex} , CA_CSN")
        mfcIndex +=1

    if ISO15693Csn:
        cfgWrite(outFile, f"APP,CT_ISO_15693, 0 , CA_CSN")

    if iClassCsn:
        cfgWrite(outFile, f"APP,CT_PICO_15693,0 , CA_CSN")
        rfIndex += 1

    if mfcCsn:
        cfgWrite(outFile, f"APP,CT_MF_CLASSIC, 0 , CA_CSN")

if leaf:
    cfgWrite(outFile, f"APP,CT_MF_DESFIRE_EV1_2, {mfcIndex} , CA_LEAF_IP")
    mfcIndex += 1

if leafSI:
    cfgWrite(outFile, f"APP,CT_MF_DESFIRE_EV1_2, {mfcIndex} , CA_MFD_DUOX")
    mfcIndex += 1
# always allow config cards in the last Ev1_2 slot
cfgWrite(outFile, f"APP,CT_MF_DESFIRE_EV1_2,{mfcIndex} , CA_FEATURES_KEYS")
mfcIndex += 1

if ev1Csn == False:
    cfgWrite(outFile, f"APP,CT_MF_DESFIRE_EV1_2, {mfcIndex} , CA_NONE")
else:
    cfgWrite(outFile, f"APP,CT_MF_DESFIRE_EV1_2, {mfcIndex} , CA_CSN")

# if not B_DEFAULT_CSN:
if ISO14443A or True: #always on for now ;)
    cfgWrite(outFile, f'RF,{rfIndex}, CP_ISO_14443A')
    rfIndex += 1

if ISO15693Csn:
    cfgWrite(outFile, f'RF,{rfIndex}, CP_ISO_15693')
    rfIndex += 1

if iClassCsn:
    cfgWrite(outFile, f'RF,{rfIndex}, CP_PICO_15693')
    rfIndex += 1

if ISO14443A or ISO15693Csn or iClassCsn or mfcCsn or ev1Csn or leaf:
    cfgWrite(outFile, "\n")
    cfgWrite(outFile, "#  13.56 MHz High Frequency RF Front End")
    cfgWrite(outFile, "OPT_AUG,OPERATION_INDEX , ENABLE_HF_RF")

if  "Standard" != mfcCsnFormat:
    cfgWrite(outFile,f"OPT, CSN_FORMAT_ISO14443A_CL1_CL2,{mfcCsnFormat} << 8")
if  "Standard" != ev1CsnFormat:
        cfgWrite(outFile,f"OPT_AUG, CSN_FORMAT_ISO14443A_CL1_CL2, {ev1CsnFormat}")
# if  "Standard" != ISO1443BcsnFormat:
        #cfgWrite(outFile,f"OPT,CSN_FORMAT_ISO14443B_FELICA, {ISO1443BcsnFormat} << 8")
# if  "Standard" != mfcCsnFormat:
        #cfgWrite(outFile,f"OPT_AUG, CSN_FORMAT_ISO14443B_FELICA, {csnFormat}")
if  "Standard" != ISO15693CsnFormat:
        cfgWrite(outFile,f"OPT,CSN_FORMAT_ISO15693_PICO15693, {ISO15693CsnFormat} << 8")
if  "Standard" != iClassCsnFormat:
        cfgWrite(outFile,f"OPT_AUG, CSN_FORMAT_ISO15693_PICO15693,{iClassCsnFormat}")


#######################################################################################
cfgWrite(outFile, "\n")
cfgWrite(outFile, "#  STEP 5: Low Frequency")
cfgWrite(outFile, "#  FSK 125 KHz Low Frequency RF Front End")
if fsk:
    cfgWrite(outFile, "OPT_AUG, OPERATION_INDEX, ENABLE_FSK_RF")
if ask:
    cfgWrite(outFile, "OPT_AUG, OPERATION_INDEX, ENABLE_ASK_RF")

if proxFilter:
    pass
    # cfgWrite(outFile, "#  Add prox filter")
    # BS_SET, FILTER, BS_FILTER_LF
    # BS_AUG, FILTER, BS_FILTER_FUNC_EQ
    # BS_SET, NUM_BITS, 35
    # BS_FILTER_MASK, 0, 0x01
    # BS_FILTER_MASK, 1, 0xFF
    # BS_FILTER_MASK, 2, 0xE0
    # BS_FILTER_MASK, 3, 0x00
    # BS_FILTER_MASK, 4, 0x00
    #
    # BS_FILTER_VALUE, 0, 0x01
    # BS_FILTER_VALUE, 1, 0x9C
    # BS_FILTER_VALUE, 2, 0x80
    # BS_FILTER_VALUE, 3, 0x00
    # BS_FILTER_VALUE, 4, 0x00

#######################################################################################
cfgWrite(outFile, "\n")
cfgWrite(outFile, "#  STEP 6: Mobile")
bleEnable = False
if 'Disabled' != bleEnable:
    cfgWrite(outFile, 'OPT_AUG, OPERATION_INDEX, ENABLE_BLE')
    if "WaveLynx (ETHS)" == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_WAVELYNX')
    elif 'AMAG (AMAG)' == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_AMAG')
    elif 'Brivo (BRVO)' == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_BRIVO')
    elif 'Fidelity (FDTY)' == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_FIDELITY')
    elif 'SafeTrust' == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_WAVELYNX')
    elif 'Unique (Differs)' == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_UNIQUE_NAME')
    elif 'Long Range (ETLR)' == bleAdv:
        cfgWrite(outFile, 'OPT_AUG, BLE_OPTIONS_2_INDEX, BLE_LR')
    if bleLegacy:
        cfgWrite(outFile, 'MOBILE, features, NFC_LEGACY_CREDENTIALS')

if 'Enabled' == nfc and 'Disabled' == mobileDESFire:
    cfgWrite(outFile, '#  NFC Support')
    cfgWrite(outFile, 'APP, CT_ISO_14443A_4, 0, CA_ANDROID_NFC')
    cfgWrite(outFile, 'APP, CT_GENERIC_CL2, 0, CA_ANDROID_NFC')
    cfgWrite(outFile, 'APP, CT_ECP_NFC, 0, CA_NONE  # ECP is disabled')
    if 'WaveLynx Transport' == mobileKey:
        cfgWrite(outFile, 'NFC_KM1_KEYS, Ck00001:KM1')
        cfgWrite(outFile, 'NFC_KC1_KEYS, Ck00001:KC1')
        cfgWrite(outFile, 'NFC_KM2_KEYS, Ck00001:KM2')
        cfgWrite(outFile, 'NFC_KC2_KEYS, Ck00001:KC2')
    elif 'AMAG Transport' == mobileKey:
        # all zeros no need to define the keys
        pass
elif 'Enabled' == nfc and 'Enabled' == mobileDESFire:
    cfgWrite(outFile,'# ECP Card type enabled')
    cfgWrite(outFile,'APP,CT_ECP_NFC,0,CA_MERIDIAN_NFC')
    cfgWrite(outFile,'# Mifare2Go Card types enabled')
    cfgWrite(outFile,'APP,CT_MF_DESFIRE_EV1_2,2,CA_M2GO_GENERIC_ACD')
    cfgWrite(outFile,'APP,CT_ISO_14443A_4,0,CA_M2GO_GENERIC_ACD')
    cfgWrite(outFile,'APP,CT_GENERIC_CL2,0,CA_M2GO_GENERIC_ACD')
    cfgWrite(outFile, '\n')
    cfgWrite(outFile,'# Removed NFC_KM# keys for Apple wallet')
    cfgWrite(outFile,f'NFC_MP0_KEYS,{leafId}:Kr0')
    cfgWrite(outFile,f'NFC_MC0_KEYS,{leafId}:Kr1')



elif 'Custom' == mobileKey and 'Disabled'== mobileDESFire:
    cfgWrite(outFile, 'MOBILE, activeKeysets, MOBILE_ACTIVE_KEYSET_SLOT1')
    cfgWrite(outFile, 'MOBILE, features, 0')
    cfgWrite(outFile, f'NFC_KM1_KEYS, {leafId}:Mkm')
    cfgWrite(outFile, f'NFC_KC1_KEYS, {leafId}:Mkc')


    

if 'On' == mobileTrans:
    #  cfgWrite(outFile, 'MOBILE_AUG, features, NFC_FEA_TRANSPORT')
     pass

if 'Enabled' == mobileDESFire and 0 == mobileTCI:
    cfgWrite(outFile,'MOBILE,ecpFormat , ECP_FORMAT_2')
    cfgWrite(outFile,'MOBILE,ecpTerminalInfoMode , ECP_WL_TERMINAL_INFO')
    cfgWrite(outFile,'MOBILE,ecpTerminalType , ECP_TERMINAL_TYPE')
    cfgWrite(outFile,'MOBILE,ecpTerminalSubType , ECP_TERMINAL_SUBTYPE_CORPORATE')
    cfgWrite(outFile,'MOBILE,ecpTCI_1 , ECP_TCI_1')
    cfgWrite(outFile,'MOBILE,ecpTCI_2 , ECP_TCI_2_DEFAULT')
    cfgWrite(outFile,'MOBILE,ecpTCI_3 , ECP_TCI_3_DEFAULT')
elif 'Enabled' == mobileDESFire and 0 != mobileTCI:
    cfgWrite(outFile, "\n")
    cfgWrite(outFile, "# ECP Format Options ")
    cfgWrite(outFile,'MOBILE,ecpFormat , ECP_FORMAT_2')
    cfgWrite(outFile,'MOBILE,ecpTerminalInfoMode , ECP_WL_TERMINAL_INFO')
    cfgWrite(outFile,'MOBILE,ecpTerminalType , ECP_TERMINAL_TYPE')
    cfgWrite(outFile,'MOBILE,ecpTerminalSubType , ECP_TERMINAL_SUBTYPE_CORPORATE')
    mobileTCI_string = str(mobileTCI)
    len_TCIstring = len(mobileTCI_string)
    mobileTCI1_1 = mobileTCI_string[0]
    mobileTCI1_2 = mobileTCI_string[1]
    mobileTCI2_1 = mobileTCI_string[2]
    mobileTCI2_2 = mobileTCI_string[3]
    mobileTCI3_1 = mobileTCI_string[4]
    mobileTCI3_2 = mobileTCI_string[5]  
    cfgWrite(outFile,f'MOBILE,ecpTCI_1,0x{mobileTCI1_1}{mobileTCI1_2}')
    cfgWrite(outFile,f'MOBILE,ecpTCI_2,0x{mobileTCI2_1}{mobileTCI2_2}')
    cfgWrite(outFile,f'MOBILE,ecpTCI_3,0x{mobileTCI3_1}{mobileTCI3_2}')
    cfgWrite(outFile,f'MOBILE,ecpBitCount,{meridianbitcount}')
    cfgWrite(outFile, "\n")
    cfgWrite(outFile, '# Mifare2Go Setup')
    cfgWrite(outFile, f'M2G_ACD_LEAF_KEYS,{leafId}:Kr4')
    cfgWrite(outFile, f'M2G_GENERIC_KEYS,{leafId}:Kr5')

    
    if ev1Csn == True:
        cfgWrite(outFile, '# EV1, EV2, EV3 CSNs are enabled in sales config sheet this will create issues in Wallet configs.')
        manualReview = True
        pass



outFile.close()

if manualReview:
    manualReviewMsg()
