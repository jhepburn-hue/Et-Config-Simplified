# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2012
# -----------------------------------------------------------------------------
#        WlTypes.h
# -----------------------------------------------------------------------------
# 
#  This file defines the data types used for firmware development.
# -----------------------------------------------------------------------------
# =============================================================================
#  This ensures all structures are packed.
FALSE                    = False
TRUE                     = True
BIT0       = 0x0001
BIT1       = 0x0002
BIT2       = 0x0004
BIT3       = 0x0008
BIT4       = 0x0010
BIT5       = 0x0020
BIT6       = 0x0040
BIT7       = 0x0080
BIT8       = 0x0100
BIT9       = 0x0200
BIT10      = 0x0400
BIT11      = 0x0800
BIT12      = 0x1000
BIT13      = 0x2000
BIT14      = 0x4000
BIT15      = 0x8000
#  Reset from normal power up
#  Reset from pin reset detected
#  Reset from application watchdog timer 0 detected
#  Reset from application CTRL-AP detected
#  Reset from application soft reset detected
#  Reset from application CPU lockup detected
#  Reset due to wakeup from System OFF mode when wakeup is triggered by DETECT signal from GPIO
#  Reset due to wakeup from System OFF mode when wakeup is triggered by ANADETECT signal from LPCOMP
#  Reset due to wakeup from System OFF mode when wakeup is triggered by entering the Debug Interface
#  Reset from network soft reset detected (Function present only in network core)
#  Reset from network CPU lockup detected (Function present only in network core)
#  Reset from network watchdog timer detected (Function present only in network core)
#  Force-OFF reset from application core detected (Function present only in network core)
#  Reset after wakeup from System OFF mode due to NFC field being detected
#  Reset from application watchdog timer 1 detected
#  Reset after wakeup from System OFF mode due to VBUS rising into valid range
#  Reset from network CTRL-AP detected (Function present only in network core)
# 
#  External Memory Data Structure
# 
EM_DM_HEADER_BLOCK_SIZE      = 256
EM_DM_HEADER_PADDING_SIZE    = 234
# 
#  Boot Loader Information Block Structure
# 
BL_INFO_BLOCK_BYTE_SIZE       = 1024
BL_INFO_BLOCK_PADDING_SIZE    = 985
KEY_SET_SIZE                  = 32
BL_READY                      = 0xA5B8
BL_EMPTY                      = 0x0000
# 
#  Structure for open nfc configuration area.
# 
NFC_META_DATA_SIZE    = 4
NFC_PADDING_SIZE      = 32
NFC_CONFIG_SIZE       = 47
# 
#  NFC config features mask
# 
NFC_FEA_TRANSPORT  = 0x01 #  disable key rolling after ~1 minute
NFC_FEA_MFG        = 0x02 #  allow wl specific credentials
NFC_LEGACY_CREDENTIALS  = 0x04 #  allow symm blue/brivo creds
#  do not encrypt credentials (brivo only)
MOBILE_LEGACY_SKIP_COMMS_ENCRYPTION  = 0x08
#  disable mypass type reads (brivo only)
MOBILE_FEA_IGNORE_MYPASS  = 0x10
MOBILE_ACTIVE_KEYSET_SLOT1  = 0x01
MOBILE_ACTIVE_KEYSET_SLOT2  = 0x02
DIVERSIFY_MC0_MASK          = 0x01
MAX_FEATURES_SIZE     = 1024
MAX_PROTOCOLS         = 16
MAX_CARD_TYPES        = 23
MAX_CARD_APPS         = 8
FILTER_MAX_BYTE_SIZE  = 8
MAX_KEY_SETS          = 16
MAX_OPTION_SETTINGS   = 64
AES_128_KEY_SIZE      = 16
MAX_KEY_PAD_BUTTONS   = 16
MAX_BLE_AD_NAME_SIZE  = 8
MAX_BIT_STREAMS_SIZE  = 32
#  Note: All fields in this structure must remain in the same exact
#        relative location to maintain legacy compatibility.
#        New fields can be added only in the rfu_1[] area.
#  The test results structure is 11 bytes in size
TEST_RESULTS_SIZE   = 11
#  Reader Types and Features
KEY_PAD_EXISTS              = 0x80
PCB15_MULLION_REV_1_0         = 0x01
PCB15_SINGLE_GANG_REV_1_0     = 0x00
HW15_PCB_REV_1_0              = 0x10
HW15_PCB_REV_UNKNOWN          = 0xFF
READER_HISTORY_SIZE			           = 256
READER_HISTORY_BLOCK_PADDING_SIZE      = 147
READER_HISTORY_BLOCK_PADDING_SIZE_2    = 65
READER_SERIAL_NUMBER_SIZE              = 8
READER_CURRENT_MEASUREMENT_SIZE        = 6
M2G_TIME_STAMP_SIZE                    = 5
ISO14443A_MAX_UID_LENGTH  = 10
ISO14443A_MAX_CASCADE_LEVELS  = 3
ISO14443B_PUPI_LENGTH  = 4
ISO14443B_APPDATA_LENGTH  = 4
ISO14443B_PROTINFO_LENGTH  = 3
ISO15693_UID_LENGTH  = 8
PICO15693_UID_LENGTH  = 8
FELICA_MAX_ID_LENGTH  = 8
OPEN_APP_BCD_LEN             = 16
OPEN_APP_BS_LEN              = 8
CIO_LEN             = 32
MFG_LEN             = 16
AUTH_CODE_LEN       = 2
CUST_ID_LEN         = 4
DIG_SIG_LEN         = 8
CRC32_LEN           = 4
#  Minimum for CRC32, Padding, Write Cmd Overhead
MAX_BUFFER_LEN  = 72
CDO_LEN             = 48
SITE_CODE_LEN       = 5
CRED_ID_LEN         = 8
PIN_LEN             = 4
MAX_CUST_DATA_LEN   = 20
CID_DATA_FILE_LEN      = 64
CID_UID_LEN            = 7
CID_CRC_LEN            = 2
CID_PERSONNEL_NO_LEN   = 7
CID_ID_NO_LEN          = 6
VISA_DATA_LEN                  = 16
VISA_PADDING_LEN1              = 7
VISA_PADDING_LEN2              = 2
VISA_CARD_NUMBER_LEN           = 2
UPS_DATA_FILE_LEN      = 9
UPS_FAC_CODE_LEN       = 4
UPS_CARD_NUMBER_LEN    = 5
LEAF_IP_ACCESS_FILE_SIZE          = 144
LEAF_IP_CAMPUS_FILE_SIZE          = 64
#  Minimum for CRC32, Padding, Write Cmd Overhead
LEAF_IP_MAX_BUFFER_LEN            = 192
LEAF_IP_ACCESS_FILE_DATA_SIZE     = 56
LEAF_IP_SITE_CODE_LEN             = 5
LEAF_IP_CRED_ID_LEN               = 8
LEAF_IP_ACCESS_DATA_LEN           = 16
LEAF_IP_PRINTED_NUMBER_LEN        = 8
LEAF_IP_ORDER_DATA_LEN            = 5
LEAF_IP_RFU_LEN                   = 9
LEAF_IP_NUM_APP_DIG_SIG           = 8
BIO_FILE_SIZE            = 2048
BIO_ACCESS_FILE_SIZE     = 96
#  Minimum for CRC32, Padding, Write Cmd Overhead
SMARTMAX_MAX_BUFFER_LEN      = 64
SMARTMAX_HEADER_LEN           = 8
SMARTMAX_SITE_CODE_LEN        = 6
SMARTMAX_CARD_NUMBER_LEN     = 10
FIPS_201_MAX_DATA           = 2048
ANDROID_MAX_DATA           = 256
MERIDIAN_MAX_BUFFER_LEN        = 128
MERIDIAN_ACCESS_CONTROL_LEN    = 16
MERIDIAN_CAMPUS_FILE_LEN       = 16
EXT_BLE_MAX_DATA_SIZE       = 512
STD_BLE_MAX_DATA_SIZE        = 64
MFC_BLOCK_SIZE              = 16
MFC_SECTOR_SIZE              = 64
M2G_FIC_LENGTH_SHORT           = 21
M2G_FIC_LENGTH_LONG            = 26
M2G_FIC_TLV_HEADER_LENGTH      = 4
M2G_FIC_PDCAP_LENGTH           = 2
M2G_FIC_UID_LENGTH             = 7
M2G_FIC_TIMESTAMP_LENGTH       = 5
#  MAX_FEATURES_SIZE + 128
FEATURES_MANAGER_FILE_SIZE  = 1252
FEATURES_COUNTDOWN_FILE_SIZE  = 4
SHARED_RAM_MAX_SIZE    = 2200
#  AudioVisualRequest
#  Disables packed structures.
LED_ACTIVE                = True
LED_INACTIVE              = False
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        WlGlobals.h
# -----------------------------------------------------------------------------
# 
#   This file contains global declarations.c
# -----------------------------------------------------------------------------
# =============================================================================
LF_IRQ_COUNT_MAX    = 5
MAX_DECIMAL_OUTPUT    = 45
MAX_RF_BUFFER_SIZE  = 96
MAX_OSDP_RX_LEN   = 1536
MAX_OSDP_TX_LEN   = 640
MAX_MCLP_RX_LEN   = MAX_OSDP_RX_LEN
MAX_MCLP_TX_LEN   = MAX_OSDP_TX_LEN
ASYNC_UART_TIMEOUT   = 3
ASYNC_UART_RETRIES   = 3
HOST_KEYPAD_BYTE_LENGTH  = 12
MAX_WIEGAND_BYTE_LENGTH    = 64
MAX_WIEGAND_BIT_LENGTH     = (MAX_WIEGAND_BYTE_LENGTH << 3)
PHY_BIT_BUFFER_SIZE  = 400
MAX_HISTORICAL_BYTES  = 15
#  Proximity Card variables
#  Proximity card data collection
PROX_DATA_BUF_MAX       = 24
PROX_HEX_DATA_MAX       = 13
#  Proximity card data storage
MAX_PROX_DATA_LEN  = 24
MAX_PROX_RAW_DATA_LEN  = 12
UNIFIED_JOB_ID_LEN  = 16
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        Features.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in Features.c.
# -----------------------------------------------------------------------------
# =============================================================================
# 
#  Product TypeDefinitions
# 
ETHOS_READER        = 1
SW_READER           = 2
IP_READER           = 3
F2F_READER          = 4
MCLP_READER         = 5
ETHOS_15_READER     = 6
LOCK_MODULE         = 7
LOCK_HUB            = 8
ETHOS_20_READER     = 9
PRODUCT_TYPE        = ETHOS_15_READER
# 
#  Build definitions (define only one)
# 
TST1_BUILD                   = 251
ECP_TEST_BUILD               = 252
ISC_WEST_BUILD               = 253
LEAF_CC_TEST_BUILD           = 254
PROD_TEST_BUILD              = 255
WAVELYNX_BUILD               = 0
EYELOCK_BUILD                = 1
WELLS_FARGO_BUILD            = 2
QUALCOMM_BUILD               = 3
DIA_BUILD                    = 4
ISONAS_BUILD                 = 5
VISA_BUILD                   = 6
ISONAS_BUILD_RC_OBSOLETE     = 7
AMAG_BUILD                   = 8
UNUSED_BUILD_9               = 9
BRIVO_BUILD                  = 10
FIDELITY_BUILD               = 11
CA_TECH_BUILD                = 12
UGA_BUILD                    = 13
UPS_BUILD                    = 14
BBH_BUILD                    = 15
SAP_BUILD                    = 16
AMAG_BoA_BUILD               = 17
LINXENS_BUILD                = 18
INTERACTIVE_BROKERS_BUILD    = 19
IBM_BUILD                    = 20
BARRY_BUILD                  = 21
DARTMOUTH_BUILD              = 22
PEPSI_BUILD                  = 23
BIORAD_BUILD                 = 24
MGH_BUILD                    = 25
MIDFIRST_BUILD               = 26
VISTRA_ENERGY_BUILD          = 27
NEW_HAVEN_BUILD              = 28
RTI_BUILD                    = 29
UTAH_BUILD                   = 30
NEVADA_BUILD                 = 31
TENET_BUILD                  = 32
TIAA_BUILD                   = 33
INOVONICS_BUILD              = 34
POUDRE_BUILD                 = 35
SCSC_BUILD                   = 36
ECP_NFC_BUILD                = 37
OPEN_OPTIONS_BUILD           = 38
UCSC_BUILD                   = 39
DIEBOLD_NIXDORF_BUILD        = 40
CITY_OF_HOPE_BUILD           = 41
AURORA_DATA_SYSTEMS_BUILD    = 42
PEPSICO_LEAFCC_BUILD         = 43
WALMART_BUILD                = 44
LEGGETT_BUILD                = 45
KETCHIKAN_BUILD              = 46
SEMPRA_ENERGY_BUILD          = 47
NEWTON_WELLESLEY_BUILD       = 48
KLA_BUILD                    = 49
EPCOR_BUILD                  = 50
SICUNET_BUILD                = 51
ZERV_BUILD                   = 52
KASTLE_BUILD                 = 53
MOCERI_BUILD                 = 54
VOLVO_BUILD                  = 55
DISH_BUILD                   = 56
AHS_BUILD                    = 57
RCC_CHIRP_BUILD              = 58
SMARTRENT_BUILD              = 59
JCI_SENSORMATIC_BUILD        = 60
SOUTH_JERSEY_BUILD           = 61
#  Version 4.1.1.FF
FW_MAJOR_VERSION              = 0x04
FW_MINOR_VERSION              = 0x02
FW_BUILD_NUMBER               = 0x02
FW_RELEASE_CANDIDATE          = 0x00
OEM_BUILD  = PROD_TEST_BUILD
FORCE_LEGACY_FEATURES_TO_DEFAULT    = 1
FORCE_LEGACY_KEYS_TO_DEFAULT        = 2
# FORCE_PROD_TEST_ON_POWER_UP        3   OBSOLETE
# DEVELOPER_BUILD                    4
READER_HISTORY_BU_ADDR  = 0x3E800
ORIGINAL_FEATURES_ADDR  = 0x3EC00
FEATURES_BACKUP_ADDR    = 0x3F000
READER_HISTORY_ADDR     = 0x3F400
FEATURES_FLASH_ADDR     = 0x3F800
BL_INFO_BLOCK_ADDR      = 0x3FC00
READER_HISTORY_BU_ADDR  = 0
# 
#  RS485 Options Masks
# 
#  SystemFeatures.OpSettings[HOST_SP_OPTIONS_INDEX] Mask Values
#  Allow up to 8 baud rates
HOST_SP_BAUD_RATE_MASK     = 0x0007
#  7 bit address, 0x00 .. 0x7E, 0x7F = Broadcast
HOST_SP_ADDR_MASK          = 0x03F8
#  Allow up to 4 RS485 protocols
HOST_SP_PROTOCOL_MASK      = 0x0C00
#  OSDP COMSET command terminates secure channel
OSDP_COMSET_KILLS_SC       = 0x1000
#  Prevent secure channel OSDP when using OSDP broadcast address
OSDP_PREVENT_SC_WITH_BA    = 0x2000
#  Prevent secure channel OSDP when SCS_15 commands are omitted.
OSDP_PREVENT_SC_NO_SCS_15  = 0x4000
# 
#  SystemFeatures.OpSettings[BLE_OPTIONS_1_INDEX]
# 
BLE_ALLOW_BOOT_LOAD_MASK        = 0x0008
BLE_BAUD_RATE_MASK              = 0x0007
BLE_PAC_APP_MASK                = 0x00F0
BLE_ALIVE_ENABLE_MASK           = 0x0800
BLE_OVERRIDE_OSDP_AV_MASK       = 0x0400
BLE_IGNORE_CREDENTIALS_MASK     = 0x0200
BLE_IGNORE_ALL_BLE_MASK         = 0x0100
BLE_ENABLE_64_BIT_FORMAT        = 0x1000
# 
#  SystemFeatures.OpSettings[KEYPAD_OPTIONS_INDEX] Mask Values
#  SystemFeatures.OpSettings[OSDP_KP_OPTIONS_INDEX] Mask Values
# 
KEYPAD_FORMAT_MASK          = 0x0007
KEYPAD_BEEP_ACTIVE_MASK     = 0x0008
KEYPAD_LED_IDLE_MASK        = 0x0010
KEYPAD_LED_ACTIVE_MASK      = 0x0020
KEYPAD_POWER_SAVE_MASK      = 0x0040
KEYPAD_LED_INVERT_MASK      = 0x0080
KEYPAD_FAC_CODE_MASK        = 0xFF00
# 
#  Feature Options Indexes
# 
OPERATION_INDEX              = 0
NEXPACS_OPTIONS_INDEX        = 1
HOST_SP_OPTIONS_INDEX        = 2
BLE_OPTIONS_1_INDEX          = 3
KEYPAD_OPTIONS_INDEX         = 4
CARD_TRACKER_TIME_OUT_INDEX  = 5
LED_OPTIONS_1_INDEX          = 6
WIEGAND_SPACE_INDEX          = 7
WIEGAND_PULSE_INDEX          = 8
BLE_TIMEOUT_MSW_INDEX        = 9
BLE_TIMEOUT_LSW_INDEX        = 10
RF_ON_EXTENSION_INDEX        = 11
BUILD_INDEX                  = 12
OSDP_KP_OPTIONS_INDEX        = 13
F2F_MCLP_INDEX               = 14
WIEGAND_DATA_OPTIONS_INDEX   = 15
CARD_DETECT_METHOD_MAX       = 16
CARD_DETECT_RANGE_PERIOD     = 17
EXT_OPERATION_INDEX          = 18
ADC_BOUNDARY_INDEX           = 19
FIPS_CHALLENGE_BYTE_INDEX    = 20
CRAUTH_CHALLENGE_BYTE        = 0xFF00
GENAUTH_CHALLENGE_BYTE       = 0x00FF
CARD_DATA_FORMAT_INDEX          = 22
ACCEL_TAMPER_SIGMA              = 23
ACCEL_TAMPER_IMMEDIATE_MASK     = 0x00FF
ACCEL_TAMPER_HISTORICAL_MASK         = 0xFF00
ACCEL_TAMPER_IMMEDIATE_DEFAULT       = 85
ACCEL_TAMPER_HISTORICAL_DEFAULT      = 15
ACCEL_TAMPER_SIGMA2             = 24
ACCEL_TAMPER_THRESHOLD_MASK     = 0x00FF
ACCEL_TAMPER_THRESHOLD_DEFAULT  = 0x19
NRF_CAP_MULLION_TUNE            = 25
NRF_CAP_SG_TUNE                 = 26
NRF_CAP_THRESHOLD_MASK          = 0x00FF
NRF_CAP_OVERSAMPLES_MASK        = 0x0700
NRF_CAP_DGAIN_MASK              = 0x3000
NRF_CAP_AGAIN_MASK              = 0xC000
NRF_CAP_THRESHOLD_DEFAULT       = 20
NRF_CAP_OVERSAMPLES_DEFAULT      = 5
NRF_CAP_DGAIN_DEFAULT            = 3
NRF_CAP_AGAIN_DEFAULT            = 1
NRF_CAP_COMMON_TUNE             = 27
# 28-29 are unused
CSN_FORMAT_ISO14443A_CL1_CL2    = 30
CSN_FORMAT_ISO14443B_FELICA     = 31
CSN_FORMAT_ISO15693_PICO15693   = 32
PROX_BITSTREAM_FORMAT           = 33
#  0: processed data,   1: raw data
PROX_BITSTREAM_STD_MASK         = BIT0
PROX_BITSTREAM_ISONAS_MASK      = BIT1
PROX_BITSTREAM_AWID_MASK        = BIT2
#  Bit stream justification for AWID
PROX_RIGHT_JUSTIFY_AWID_MASK    = BIT3
#  For 48-bit prox only,   0: disabled,  1:enabled
PROX_ENABLE_48_BIT_MASK         = BIT4
#  For AWID, ISONAS, and STD   0: enabled,  1:disabled
PROX_DISABLE_ISONAS_MASK        = BIT5
PROX_DISABLE_AWID_MASK          = BIT6
PROX_DISABLE_STD_MASK           = BIT7
RF_POLL_TIMEOUT                 = 34
NEXPACS_APP_SETTINGS_1_INDEX    = 35
NEXPACS_APP_SETTINGS_2_INDEX    = 36
#  SystemFeatures.OpSettings[OPERATION_INDEX] Mask Values
ENABLE_HIGHER_RF_BAUDRATES        = (BIT0 | BIT1)
ENABLE_ASK_RF		              = BIT2
ENABLE_FSK_RF                     = BIT3
ENABLE_HF_RF                      = BIT4
ENABLE_BLE                        = BIT5
ENABLE_BLE_RESET_BUGFIX           = BIT6
#  HOST_INTERFACE_MASK is no longer used
TAMPER_INITIATES_OSDP_DEF         = BIT6
DISABLE_CARD_TRACKER              = BIT7
ENABLE_TAMPER_CNTRL_LINE          = BIT8
ENABLE_TAMPER_EVENTS              = BIT9
ENABLE_HOST_CNTL_AV               = BIT10
ENABLE_HOST_CNTL_AV_EXCLUSIVE     = BIT11
ENABLE_TAMPER_AUDIO_ALARM         = BIT12
ENABLE_INCLUDE_CSN_ACCESS_DATA    = BIT13
REPORT_TAMPER_STATE_CHANGE_ONLY   = BIT14
OSDP_AUTO_DETECT_ACTIVE           = BIT15
#  SystemFeatures.OpSettings[EXT_OPERATION_INDEX] Mask Values
ENABLE_MTI_ASK_RF                 = BIT0
IGNORE_PROXIMITY_CARDS            = BIT1
INVERT_TAMPER_STATE               = BIT2
TAMPER_INITIATES_OSDP_AUTO        = BIT3
OSDP_SCBK_LOADED                  = BIT4
OSDP_SCBK_EXCLUSIVE               = BIT5
FAST_HF_POLL_FREQUENCY            = BIT6
SILENCE_BEEPER                    = BIT7
TAMPER_STABILITY_COUNT_MASK       = 0x0F00
TAMPER_ACTIVE_COUNT_MASK          = 0xF000
#  SystemFeatures.OpSettings[F2F_MCLP_INDEX] Mask Values
MCLP_READER_TYPE_MASK             = BIT0
USE_CSN_BCD_FORMAT_MASK           = BIT1
USE_ASK_BCD_FORMAT_MASK           = BIT2
USE_BLE_BCD_FORMAT_MASK           = BIT3
USE_40_BIT_BCD_FORMAT_MASK        = BIT4
XMIT_FW_BUILD_MASK                = BIT5
USE_NFC_BCD_FORMAT_MASK           = BIT6
USE_BYTE_STUFF_IN_CS_MASK         = BIT7
FT_TIMEOUT_MASK                   = 0xFF00
CARD_AV_OPTIONS_1_INDEX         = 37
#  SystemFeatures.OpSettings[CARD_AV_OPTIONS_1_INDEX] Mask Values
CARD_AV_BEEPER_ENABLED          = 0x8000
CARD_AV_BEEP_DURATION_MASK      = 0x07FF
CARD_AV_OPTIONS_2_INDEX         = 38
#  SystemFeatures.OpSettings[CARD_AV_OPTIONS_2_INDEX] Mask Values
CARD_AV_LED_ENABLED             = 0x8000
CARD_AV_LED_DURATION_MASK       = 0x07FF
CARD_AV_PROGRESS_LED_ENABLED    = 0x0800
CARD_AV_PROGRESS_DURATION_MASK  = 0x7000
SENSITIVITY_INDEX               = 39
#  SystemFeatures.OpSettings[SENSITIVITY_INDEX] Mask Values
OSDP_LATE_RESPONSE_TIME_MASK    = 0x00FF
ACC_SENSITIVITY_MASK            = 0x0F00
HF_GAIN_MASK                    = 0xF000
FIPS_201_INDEX                  = 40
#  SystemFeatures.OpSettings[FIPS_201_INDEX] Mask Values
FIPS_201_ACCESS_DATA_FORMAT     = 0x001F
FIPS_201_FORCE_GUID             = 0x0020
FIPS_201_USE_VSTAT_REPLY        = 0x0040
FIPS_201_INCLUDE_TLV_HEADER     = 0x0080
FIPS_201_EXT_RF_PERSIST         = 0x0100
FIPS_201_DISABLE_INID           = 0x0200
FEATURE_COUNT_DOWN_INDEX        = 41
FEATURE_COUNT_DOWN_MINUTES      = 0x001F
LED_OPTIONS_2_INDEX             = 42
#  SystemFeatures.OpSettings[LED_OPTIONS_2_INDEX] Mask Values
PIN_ENTRY_COLOR_MASK              = 0x0700
BLUE_LED_IDLE_COLOR_MASK          = 0x8000
BLUE_LED_CARD_AV_COLOR_MASK       = 0x4000
ALLOW_STACKED_OSDP_AV_CMDS_MASK   = 0x2000
OSDP_REVERSE_RED_GREEN_LED_MASK   = 0x0800
PIN_BLINK_DURATION_MASK           = 0x00FF
LED_OPTIONS_3_INDEX             = 43
#  SystemFeatures.OpSettings[LED_OPTIONS_3_INDEX] Mask Values
PIN_ENTRY_DURATION_MASK         = 0x003F
LED_CONTROL_LINES_MASK          = 0x00C0
LED_DRIVER_GAIN_MASK            = 0xFF00
SE_INDEX                        = 44
#  SystemFeatures.OpSettings[SE_INDEX] Mask Values
SE_DISABLED_MASK                 = 0x0001
SE_DISCOVERED_MASK               = 0x0002
SE_KEYS_TRANSFERRED_MASK         = 0x0004
SE_OBSOLETE_DO_NOT_USE_MASK1     = 0x0008
SE_KEY_VER_MASK                  = 0x0030
SE_OBSOLETE_DO_NOT_USE_MASK2     = 0x0040
SE_CHECK_IF_POPULATED_MASK       = 0x0080
SE_DISPLAY_ERROR_AV_MASK         = 0x0100
LEAF_IP_DEF_INDEX               = 45
LEAF_IP_KS1_INDEX               = 46
LEAF_IP_KS2_INDEX               = 47
LEAF_IP_KS3_INDEX               = 48
LEAF_IP_READ_KEY_MASK           = 0x003F
LEAF_IP_IGNORE_KEYSET_MASK      = 0x4000
BLE_OPTIONS_2_INDEX             = 49
#  SystemFeatures.OpSettings[BLE_OPTIONS_2_INDEX] Mask Values
BLE_CONFIG_SETTING_MASK         = 0x00FF
LOCK_RELOCK_DELAY_INDEX         = 50
LOCK_MOTOR_ON_TIME_INDEX        = 51
LOCK_FAIL_STATE_INDEX           = 52
DEFAULT_RELOCK_DELAY           = 4000
DEFAULT_LOCK_MOTOR_ON_TIME     = 700
FAIL_AS_IS                     = 0
FAIL_SECURE                    = 1
FAIL_SAFE                      = 2
LED_BAR_1_INDEX                = 53
LED_BAR_CARD_AV_MASK           = 0x0003
LED_BAR_CARD_PROGRESS_MASK     = 0xC000
LED_BAR_U_IDLE_COLOR_MASK      = 0x001C
LED_BAR_U_IDLE_FUNCTION_MASK   = 0x00E0
LED_BAR_L_IDLE_COLOR_MASK      = 0x0700
LED_BAR_L_IDLE_FUNCTION_MASK   = 0x3800
LED_BAR_2_INDEX                = 54
RED_CNTRL_COLOR_MASK           = 0x0007
RED_CNTRL_LED_BAR_MASK         = 0x0018
GREEN_CNTRL_COLOR_MASK         = 0x00E0
GREEN_CNTRL_LED_BAR_MASK       = 0x0300
OSDP_CNTRL_LED_BAR_MASK        = 0x0C00
MFC_APP_INDEX                  = 55
MFC_APP_SECTOR_MASK            = 0x00FF
MFC_KEY_DIV_MASK               = BIT8
MFC_USE_KEY_B_MASK             = BIT9
DEF_TAMPER_CONFIG_INDEX        = 56
TAMPER_COUNTDOWN_MASK          = 0x0FFF
TAMPER_DEVICE_MASK             = 0x3000
OSDP_VENDOR_CODE_VC1_INDEX     = 57
OSDP_VENDOR_CODE_VC2_3_INDEX   = 58
OSDP_VENDOR_CODE_1_MASK        = 0x00FF
OSDP_VENDOR_CODE_2_MASK        = 0xFF00
OSDP_VENDOR_CODE_3_MASK        = 0x00FF
SPECIAL_FEATURES_INDEX         = 59
#  SystemFeatures.OpSettings[SPECIAL_FEATURES_INDEX] Mask Values
ENABLE_RF_AUTO_GAIN            = 0x0001
ENABLE_EXCLUSIVE_HOST_LOAD     = 0x0002
LEAF_IP_SKIP_SIG_MASK          = 0x0004
LEAF_IP_SKIP_HS_FILE_MASK      = 0x0008 #  do not remove needed for legacy configs
BUILD_EXT_MASK                 = 0x0300 #  extends build mask to include up to 1024 builds
DISABLE_RETURN_TO_FACTORY_DEFAULTS   = 0x0010
CAPTOUCH_FEATURES_INDEX        = 60
CAPTOUCH_EVENT_TRIGGER_LEVEL   = 61
#  SystemFeatures.OpSettings[CAPTOUCH_FEATURES_INDEX] Mask Values
CAPTOUCH_EVENT_CHAR_MASK       = 0xFF00
CAPTOUCH_UNUSED_MASK           = 0x00FC
CAPTOUCH_ENABLED_MASK          = 0x0001
CAPTOUCH_AV_ENABLED_MASK       = 0x0002
CUSTOMER_PERMISSIONS		   = 62
#  SystemFeatures.OpSettings[CUSTOMER_PERMISSIONS] Values
CUSTOMER_OSDP_ENABLE			 = 0x8000
CUSTOMER_ENCRYPTED_ENABLE		 = 0x4000
#  The CUSTOMER PERMISSIONS MASK will allow individual commands to pass through or be blocked.
#  Works out to taking 1 << by the tag
CUSTOMER_PERMISSIONS_LED 			 = 1 << 1
CUSTOMER_PERMISSIONS_BUZZ 			 = 1 << 2
CUSTOMER_PERMISSIONS_TECHNOLOGY 	 = 1 << 3
CUSTOMER_PERMISSIONS_CREDENTIALS	 = 1 << 4
CUSTOMER_PERMISSIONS_MOBILE 		 = 1 << 5
CUSTOMER_PERMISSIONS_ECP 			 = 1 << 6
CUSTOMER_PERMISSIONS_KEYS 			 = 1 << 7
CUSTOMER_PERMISSIONS_RTFD 			 = 1 << 8
CUSTOMER_PERMISSIONS_OSDP 			 = 1 << 9
CUSTOMER_PERMISSIONS_MASK			 = 0x3FFF
NEXPACS_APP_SETTINGS_3_INDEX      = 63
NEXPACS_FILE_LEN_MASK             = 0x00FF
#  SystemFeatures.OpSettings[CARD_DATA_FORMAT_INDEX] Mask Values
CARD_DATA_FULL_BIT_STREAM       = BIT0
CARD_DATA_FACILITY_SITE_CODE    = BIT1
CARD_DATA_ID_CODE               = BIT2
CARD_DATA_INVERT_BITS           = BIT3
CARD_DATA_REVERSE_BITS          = BIT4
CARD_DATA_REVERSE_BYTES         = BIT5
CARD_DATA_JUSTIFICATION         = BIT6
CARD_DATA_HEXIDECIMAL           = BIT7
CARD_DATA_DECIMAL               = BIT8
CARD_DATA_BINARY                = BIT9
CARD_BID_PASS_REJECT            = BIT10
CARD_BCD_ENABLE                 = BIT11
BID_RANGE_REJECT                = 0
BID_RANGE_PASS                  = BIT10
#  SystemFeatures.OpSettings[CARD_DATA_FORMAT_INDEX] Mask Values for SWH app and Dorma Kaba app
SWH_START_BIT_MASK              = 0xFF00
SWH_NUM_BITS_MASK               = 0x00FF
#  SystemFeatures.OpSettings[CARD_DATA_PARITY_STRIP_INDEX] Mask Values
STRIP_LEADING_BITS_MASK         = 0x00F0
STRIP_TRAILING_BITS_MASK        = 0x000F
#  SystemFeatures.OpSettings[LED_OPTIONS_1_INDEX] Mask Values
#  See SystemFeatures.OpSettings[LED_OPTIONS_2_INDEX] for more blue LED options
LED_IDLE_COLOR_MASK             = 0x0003
LED_CARD_AV_COLOR_MASK          = 0x000C
RED_LED_PWM_DUTY_CYCLE_MASK     = 0x00F0
GREEN_LED_PWM_DUTY_CYCLE_MASK   = 0x0F00
BLUE_LED_PWM_DUTY_CYCLE_MASK    = 0xF000
#  Defaults
#   Blue LED PWM = 50% (5)
#   Green LED PWM = 50% (5)
#   Red LED PWM = 60% (6)
DEFAULT_LED_PWM_DUTY_CYCLES     = 0x5560
#  SystemFeatures.KgMap MASK Values
#  Indicates valid key components have been created.
KG_ACTIVE             = 0x01
KG1_ACTIVE            = 0x02
KG2_ACTIVE            = 0x04
KG2_SKIP              = 0x80
#  Index into configuration data where key storage begins
KEY_STORAGE_INDEX            = 494
# 
#  Bit Operations
# 
BIT_OP_CLEAR            = 1
BIT_OP_SET              = 2
BIT_OP_TOGGLE           = 3
#  SystemFeatures.OpSettings[BUILD_INDEX] Masks and Build Values
FW_RF_AUTO_TUNE_MASK          = 0x0800
FW_BLE_AV_ACTION_MASK         = 0x0400
FW_BLE_AV_COLOR_MASK          = 0x0300
FW_BLE_AV_PERIOD_MASK         = 0xF000
FW_BUILD_MASK                 = 0x00FF
FW_BUILD_WAVELYNX_CWL1        = 0x00
FW_BUILD_EYELOCK              = 0x01
FW_BUILD_WELLS_FARGO_CWF1     = 0x02
FW_BUILD_QUALCOMM_CQU1        = 0x03
FW_BUILD_DIA                  = 0x04
FW_BUILD_ISONAS_W             = 0x05
FW_BUILD_VISA_CVA1            = 0x06
FW_BUILD_ISONAS_RC            = 0x07
#  U001_1 = CAM1 for Mercedes  (production label change only)
FW_BUILD_AMAG_CAM1            = 0x08
FW_BUILD_UNUSED_9             = 0x09
FW_BUILD_BRIVO_CBR1           = 0x0A
FW_BUILD_FIDELITY_CFA2        = 0x0B
FW_BUILD_CA_TECH_CCA1         = 0x0C
FW_BUILD_UGA_CUG1             = 0x0D
FW_BUILD_UPS_U006_1           = 0x0E
FW_BUILD_BBH_CBB1             = 0x0F
FW_BUILD_SAP                  = 0x10
FW_BUILD_AMAG_CBA1            = 0x11
FW_BUILD_LINXENS              = 0x12
FW_BUILD_INTERACTIVE_CIB1     = 0x13
FW_BUILD_IBM_CIM1             = 0x14
FW_BUILD_BARRY_CBU1           = 0x15
FW_BUILD_DARTMOUTH_CDM1       = 0x16
FW_BUILD_PEPSI_U007_1         = 0x17
FW_BUILD_BIORAD_CBIO1         = 0x18
FW_BUILD_MGH_CMG1             = 0x19
FW_BUILD_MIDFIRST_CMF1        = 0x1A
FW_BUILD_VISTRA_ENERGY_CVE1   = 0x1B
FW_BUILD_NEW_HAVEN_CNH1       = 0x1C
FW_BUILD_RTI_CRT1             = 0x1D
FW_BUILD_UTAH_CSU1            = 0x1E
FW_BUILD_NEVADA_CSN1          = 0x1F
FW_BUILD_TENET_CTH1           = 0x20
FW_BUILD_TIAA_CTI1            = 0x21
FW_BUILD_INOVONICS_CIN1       = 0x22
FW_BUILD_POUDRE_CPS1          = 0x23
FW_BUILD_UNUSED_36            = 0x24
FW_BUILD_UNUSED_37            = 0x25
FW_BUILD_OPEN_OPTIONS_COO1    = 0x26
FW_BUILD_UCSC_CUC1            = 0x27
FW_BUILD_DIEBOLD_CDN1         = 0x28
FW_BUILD_CITY_OF_HOPE_CCH1    = 0x29
FW_BUILD_AURORA_DATA_SYSTEMS_CAS1   = 0x2A
FW_BUILD_PEPSICO_CPE1         = 0x2B
FW_BUILD_WALMART_CWM1         = 0x2C
FW_BUILD_LEGGETT_CLP1         = 0x2D
FW_BUILD_KETCHIKAN_CKI1       = 0x2E
FW_BUILD_SEMPRA_ENERGY_CSP1   = 0x2F
FW_BUILD_NEWTON_WELLESLEY_CNW1  = 0x30
FW_BUILD_KLA_CKL1             = 0x31
FW_BUILD_EPCOR_CEP1           = 0x32
FW_BUILD_SICUNET_CSI1         = 0x33
FW_BUILD_ZERV_CZE1            = 0x34
FW_BUILD_KASTLE_CKA1          = 0x35
FW_BUILD_MOCERI_CMM1          = 0x36
FW_BUILD_VOLVO_CVV1           = 0x37
FW_BUILD_DISH_CDC1            = 0x38
FW_BUILD_AHS_CAH1             = 0x39
FW_BUILD_SICUNET_CSI2         = 0x3A
FW_BUILD_RCC_CHIRP_CRC1       = 0x3B
FW_BUILD_4th_IQ_CSR1          = 0x3C
FW_BUILD_PDK_CPK1             = 0x3D
FW_BUILD_UPS_U006_2           = 0x3E
FW_BUILD_ALARM_CAL1           = 0x3F
FW_BUILD_SMARTRENT_CSR1       = 0x40
FW_BUILD_COINBASE_CCS1        = 0x41
FW_BUILD_SRC_CSC1             = 0x42
FW_BUILD_BLINE_CBL1           = 0x43
FW_BUILD_OKLAHOMA_CCK1        = 0x44
FW_BUILD_INOVONICS_CIN2       = 0x45
FW_BUILD_JERSEY_CSJ1          = 0x46
FW_BUILD_NAVAHO_PREP_CNP1     = 0x47
FW_BUILD_CHESAPEAKE_CCC1      = 0x48
FW_BUILD_PAREXCEL_CPX1        = 0x49
FW_BUILD_MICHIGAN_CD_CMD1     = 0x4A
FW_BUILD_OKLAHOMA_COH1        = 0x4B
FW_BUILD_AMAG_CAM4            = 0x4C
FW_BUILD_WESTERN_DIGITAL_CWD1  = 0x4D
FW_BUILD_JCI_SENSORMATIC_CSE1  = 0x4E
FW_BUILD_DOOR_DASH_CDD1       = 0x4F
FW_BUILD_STOCKTON_CSM1        = 0x50
FW_BUILD_GENEA_CGN1           = 0x51
FW_BUILD_BUTTERFLYMX_CBF1     = 0x52
FW_BUILD_RED_HAT_CRH2         = 0x53
FW_BUILD_TARGET_CTG1          = 0x54
FW_BUILD_MTI_CMT1             = 0x55
FW_BUILD_WAVELYNX_CPV1        = 0x80
FW_BUILD_WAVELYNX_CWL2        = 0x81
FW_BUILD_WELLS_FARGO_CWA      = 0x82
FW_BUILD_AMAG_CAM2            = 0x83
FW_BUILD_SAFETRUST_CST1       = 0x84
FW_BUILD_TRANSPARENT_XRW      = 0x85
FW_BUILD_AMAG_CBA2            = 0x86
FW_BUILD_AMAG_CBA3            = 0x87
FW_BUILD_AMAG_CF21            = 0x88
FW_BUILD_WL_CF22              = 0x89
FW_BUILD_BRIVO_CBR2           = 0x8A
FW_BUILD_AMAG_CMC1            = 0x8B
FW_BUILD_MGH_CMG2             = 0x8C
FW_BUILD_ZERV_CZE2            = 0x8D
FW_BUILD_NEWTON_WELLESLEY_CNW2   = 0x8E
FW_BUILD_BBH_CBB2             = 0x8F
FW_BUILD_IBM_CIM9             = 0x90
FW_BUILD_AMAG_CMC2            = 0x91
FW_BUILD_AMAG_CAM3            = 0x92
FW_BUILD_KASTLE_CKA2          = 0x93
FW_BUILD_WAVELYNX_CWL3        = 0x94
FW_BUILD_WAVELYNX_CPV2        = 0x95
FW_BUILD_KASTLE_CKA3          = 0x96
FW_BUILD_IBM_CIM2             = 0x97
FW_BUILD_UNUSED_152           = 0x98
FW_BUILD_RED_HAT              = 0x99
FW_BUILD_BRIVO_CBR3           = 0x9A
FW_BUILD_KASTLE_CKA4          = 0x9B
FW_BUILD_AMAG_CBA4            = 0x9E
FW_BUILD_BRIVO_CBR4           = 0xAA
FW_BUILD_BRIVO_CBR5           = 0xBA
FW_BUILD_WAVELYNX_CWL9        = 0xF9
FW_BUILD_SAMPLE1              = 0xFA
FW_BUILD_TST1                 = 0xFB
FW_BUILD_ECP_TEST             = 0xFC
FW_BUILD_ISC_WEST             = 0xFD
FW_BUILD_LEAF_CC_TEST         = 0xFE
FW_BUILD_PROD_TEST            = 0xFF
# 
#  SystemFeatures.OpSettings[NEXPACS_OPTIONS_INDEX] Mask Values
# 
SKIP_CIO                           = BIT0
SKIP_SIGNATURE_CHECK               = BIT1
SEND_ALL_NEXPACS_DATA              = BIT2
SEND_NEXPACS_SITE_CODE             = BIT3
SEND_NEXPACS_CREDENTIAL_ID         = BIT4
USE_ISO7816_WRAPPER                = BIT5
PRE_SELECT_DF_NAME                 = BIT6
NEXPACS_AID_B2_MASK                = 0xF000
NEXPACS_KEYSET_MASK                = 0x0F00
NEXPACS_KEYSET_DEF                 = 0x0000
NEXPACS_KEYSET_1                   = 0x0100
NEXPACS_KEYSET_2                   = 0x0200
NEXPACS_KEYSET_3                   = 0x0300
# 
#  SystemFeatures.OpSettings[NEXPACS_APP_SETTINGS_1_INDEX] Mask Values
# 
NEXPACS_AID_B0_MASK                = 0xFF00
NEXPACS_AID_B1_MASK                = 0x00FF
# 
#  SystemFeatures.OpSettings[NEXPACS_APP_SETTINGS_2_INDEX] Mask Values
# 
NEXPACS_AID_2_MASK                = 0xFF00
NEXPACS_FILE_NUM_MASK             = 0x00F0
NEXPACS_SKIP_APP_LIST_MASK        = 0x0001
NEXPACS_TRY_OTHER_KEY_MASK        = 0x0002
# 
#  SystemFeatures.OpSettings[WIEGAND_DATA_OPTIONS_INDEX] Mask Values
# 
WIEGAND_INCLUDE_SOURCE_OBSOLETE    = BIT0
WIEGAND_ENABLE_DUAL_AUTH_OBSOLETE  = BIT1
WIEGAND_CASI_4001_2_MASK           = BIT2
F2F_IBM_MASK                       = BIT3
F2F_OP_STATE_MASK                  = (BIT4 | BIT5)
AP_MAX_CARD_CNT_MASK               = 0x0F00
WIEGAND_TRANSMIT_POR               = BIT14
WIEGAND_INVERT_D0_D1               = BIT15
WIEGAND_CASI_4001                  = 0
WIEGAND_CASI_4002                  = BIT2
F2F_UNSUPERVISED_STATE             = 0
F2F_2_STATE                        = BIT4
F2F_4_STATE                        = BIT5
ROTATE_CASI                        = 1
ROTATE_F2F                         = 2
D0_GRN_LED_BOUNDARY                = 0x94D
# 
#  EV1 Application ID for the features manager application (51CD)
# 
FEATURES_MANAGER_AID_B0      = 0xF5
FEATURES_MANAGER_AID_B1      = 0x1C
FEATURES_MANAGER_AID_B2      = 0xD0
FEATURES_MANAGER_FILE_NUM    = 1
FEATURES_COUNT_FILE_NUM      = 2
FEATURES_COUNTDOWN_FILE_NUM  = 3
# 
#  Supported Card RF Protocols
# 
CP_NONE                = 0
CP_ISO_14443A          = 1
CP_ISO_14443B          = 2
CP_ISO_15693           = 3
CP_PICO_15693          = 4
CP_FELICA              = 5
# 
#  Supported Card Types
# 
CT_UNKNOWN             = 0
CT_ISO_14443A_3        = 1
CT_ISO_14443A_4        = 2
CT_MF_CLASSIC          = 3
CT_MF_ULTRALIGHT       = 4
CT_GENERIC_CL2         = 5
CT_MF_DESFIRE_EV1_2    = 6
CT_MF_PLUS_S           = 7
CT_MF_PLUS_X           = 8
CT_ISO_14443B          = 9
CT_ISO_15693           = 10
CT_PICO_15693          = 11
CT_FELICA              = 12
CT_ECP_NFC             = 13
MAX_VALID_CARD_TYPES   = 14
# 
#  Supported Card Applications
# 
CA_NONE                = 0x00
CA_CSN                 = 0x01
CA_NEXPACS             = 0x02
CA_FEATURES_KEYS       = 0x03
CA_FIPS_201_1          = 0x04
CA_EYELOCK_TOC         = 0x05
CA_VISA_MFC_APP        = 0x06
CA_LEAF_IP             = 0x07
CA_MFC_SMARTMAX        = 0x08
CA_MFD_SMARTMAX        = 0x09
CA_MFC_FIDELITY        = 0x0A
# CA_MFD_FIDELITY       0x0B
CA_DAIMLER_CID         = 0x0C
CA_UPS                 = 0x0D
CA_TRANSPARENT_XRW     = 0x0E
CA_BARRY               = 0x0F
CA_ANDROID_NFC         = 0x10
CA_OBSOLETE            = 0x11
CA_MERIDIAN_NFC        = 0x12
CA_OPEN_BCD            = 0x13
CA_KASTLE_APDU_APP     = 0x14
CA_MFC_SWH             = 0x15
CA_MFD_SWH             = 0x16
CA_M2GO_LEAF_ACD       = 0x17
CA_M2GO_GENERIC_ACD    = 0x18
CA_DORMA_KABA          = 0x19
CA_MFC_ACTPRO          = 0x1A
CA_MFD_ACTPRO          = 0x1B
CA_MFD_DUOX            = 0x1C
# 
#  ISO 7816-6/AM1
#  In CL2 ISO14443A cards, UID0 indicates the manufacturer ID.
#  For example, NXP cards have 0x04 as the value in UID0.
# 
#  0x00 Not Specified
#  0x01 Motorola
#  0x02 ST Microelectronics
#  0x03 Hitachi, Ltd
#  0x04 NXP Semiconductors
#  0x05 Infineon Technologies AG
#  0x06 Cylink
#  0x07 Texas Instrument
#  0x08 Fujitsu Limited
#  0x09 Matsushi*ta Electronics Corporation (remove *, the forum doesn't like the resulting word fraction)
#  0x0A NEC
#  0x0B Oki Electric Industry Co. Ltd
#  0x0C Toshiba Corp.
#  0x0D Mitsubishi Electric Corp.
#  0x0E Samsung Electronics Co. Ltd
#  0x0F Hyundai Electronics Industries Co. Ltd
#  0x10 LG-Semiconductors Co. Ltd
#  0x11 Emosyn-EM Microelectronics
#  0x12 INSIDE Technology
#  0x13 ORGA Kartensysteme GmbH
#  0x14 SHARP Corporation
#  0x16 EM Microelectronic-Marin SA
#  0x17 KSW Microtec GmbH
#  0x18	ZMD AG (DE)
#  0x19 XICOR, Inc.
#  0x20	Renesas Technology Corp (JP)
#  0x21	TAGSYS (FR)
#  0x22	Transcore (US)
#  0x23	Shanghai Belling Corp Ltd (CN)
#  0x24	Masktech Germany GmbH (DE)
#  0x25	Innovision Research and Technology Plc (UK)
#  0x26	Hitachi ULSI Systems Co Ltd (JP)
#  0x27	Cypak AB (SE)
#  0x28	Ricoh (JP)
#  0x29	ASK (FR)
#  0x2A	Unicore Microsystems LLC (RU)
#  0x2B Dallas Semiconductor/Maxim
#  0x2C	Impinj Inc (US)
#  0x2D	RightPlug Alliance (US)
#  0x2E	Broadcom Corporation (US)
#  0x2F	MStar Semiconductor Inc (TW)
#  0x30	BeeDar Technology Inc (US)
#  0x31	RFIDsec (DK)
#  0x32	Schweizer Electronic AG (DE)
#  0x33	AMIC Technology Corp (TW)
#  0x34	Mikron JSC (RU)
#  0x35	Fraunhofer Institute for Photonic Microsystems (DE)
#  0x36	IDS Microship AG (CH)
#  0x37	Kovio (US)
#  0x38	AHMT Microelectronic Ltd (CH)
#  0x39	Silicon Craft Technology (TH)
#  0x3A	Advanced Film Device Inc. (JP)
#  0x3B	Nitecrest Ltd (UK)
#  0x3C	Verayo Inc. (US)
#  0x3D	HD Global (US)
#  0x3E	Productivity Engineering Gmbh (DE)
#  0x3F Austria Micro Systems (AMS)
#  0x40	Gemalto SA (FR)
#  0x41	Renesas Electronics Corporation (JP)
#  0x42	3Alogics Inc (KR)
#  0x43	Top TroniQ Asia Limited (Hong Kong)
#  0x44	Gentag Inc (USA)
# 
#  Function like Macros
# 
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2015
# -----------------------------------------------------------------------------
#        Ble.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in Ble.c
# -----------------------------------------------------------------------------
# =============================================================================
BLE_PING                      = 0x20
BLE_FCC_TEST_MODE             = 0x2B
BLE_TIMEOUT_STATUS            = 0x2C
BLE_ALIVE                     = 0x2D
BLE_MFG_TEST_CMD              = 0x2E
BLE_MFG_TEST_RSP              = 0x2F
# 
#  USB Response Values
# 
BLE_RSP_SUCCESS              = 0x00
BLE_RSP_FAILED               = 0x01
BLE_FIELD_OUT_OF_RANGE       = 0x07
BLE_INCORRECT_SETUP          = 0x0A
BLE_CRC_FAILURE              = 0x0B
BLE_MSG_RESPONSE              = 0x5C
BLE_GET_SERIAL_NUMBER_TAG     = 0x60
BLE_TAG_UNUSED61              = 0x61
BLE_TAG_UNUSED62              = 0x62
BLE_GET_READER_DETAILS_TAG    = 0x63
BLE_SET_OSDP_ADDRESS_TAG      = 0x64
BLE_SET_OSDP_KEY_TAG          = 0x65
BLE_SET_OSDP_BAUD_TAG         = 0x66
BLE_PROCESS_EM_DATA           = 0x6A
BLE_CLEAR_EM_DATA             = 0x6B
BLE_ENCRYPT_STORE_DATA        = 0x6C
BLE_GET_EM_DATA               = 0x6D
BLE_PUT_EM_DATA               = 0x6E
BLE_DEVICE_UID_TAG            = 0x70
BLE_SET_ADVERTISED_NAME_TAG   = 0x71
BLE_GET_VERSION_TAG           = 0x72
BLE_SET_APP_TIMEOUT_TAG       = 0x73
BLE_AV_CONTROL_TAG            = 0x74
BLE_SELF_ENROLL_TAG           = 0x75
BLE_SET_CONFIG_TAG            = 0x76
BLE_CONNECT_LED_BLINK_TAG     = 0x77
# BLE_MPD_MESSAGE_TAG          0x78
BLE_CLEAR_USER_SPACE_TAG      = 0x78
BLE_MPD_KEY_TAG               = 0x79
BLE_ACTIVTY_DETECTED_TAG      = 0x7A
BLE_BITSTREAM_FORMAT_TAG      = 0x7B
BLE_SEND_READER_INFO_TAG      = 0x7C
BLE_KEY                       = 0x7D
BLE_GET_READER_CONFIG_TAG     = 0x7E
BLE_IBEACON_CONFIG_TAG        = 0xB0
TAG_AV3_MODE_INIT             = 0xB1
TAG_AV3_CONNECTION            = 0xB2
TAG_AV3_DISCONNECT            = 0xB3
TAG_AV3_CMD                   = 0xB4
TAG_AV3_RSP                   = 0xB5
TAG_AV3_STATUS                = 0xB6
AV3_INIT_LEGACY_CREDENTIALS   = 0x01
BLE_IBEACON_TRIGGER_TAG       = 0xBA
BLE_IBEACON_CONFIG_RETRIES    = 3
BLE_OPSETTINGS                = 0x90
BLE_OPSETTINGS_DATA_SIZE      = 222
BLE_OPSETTINGS_PACKET_SIZE    = 224
BLE_CARD_TYPES_APPS           = 0x91
BLE_CARD_TYPES_DATA_SIZE      = 272
BLE_CARD_TYPES_PACKET_SIZE    = 272
BLE_OFF     = 0
BLE_ON      = 1
BLE_MAX_PACKET_LEN            = 100
BLE_MIN_IBEACON_CONFIG_LEN    = 23
# 
#  Supported BLE Physical Access Applications
# 
BLE_PAC_NONE           = 0x00
BLE_PAC_NEXPACS        = 0x01
BLE_PAC_DEVICE_UID     = 0x02
BLE_PAC_EYELOC_TOC     = 0x03
#  Note BLE_PAC_FIDELITY is obsolete
BLE_PAC_FIDELITY       = 0x04
# 
#  Supported BLE Application Modes
# 
BLE_MODE_PASS_THROUGH    = 0x4E
BLE_MODE_BUTTON_PRESS    = 0x42
BLE_MODE_PIN_ENRTY       = 0x50
# 
#  Supported BLE Config Type Definitions
# 
BLE_WAVELYNX           = 0
BLE_AMAG               = 1
BLE_BRIVO              = 2
BLE_ISONAS             = 3
BLE_FIDELITY           = 4
BLE_FIDELITY_BLUELYNX  = 5
BLE_WAVELYNX_SR        = 6
BLE_LR                 = 8
BLE_UNIQUE_NAME        = 9
BLE_NONE               = 0xFF
BLE_DEFAULT_TIMEOUT      = 10000
IBEACON_TRIGGER_TOUCH     = 1
IBEACON_TRIGGER_KEYPAD    = 2
IBEACON_TRIGGER_OSDP_MSG  = 4
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2014
# -----------------------------------------------------------------------------
#        Leds.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in Leds.c
# -----------------------------------------------------------------------------
# =============================================================================
LED_OFF    = 0
LED_ON     = 1
BLACK_LED              = 0
RED_LED                = 1
GREEN_LED              = 2
RED_GREEN_LEDS         = 3
BLUE_LED               = 4
RED_BLUE_LEDS          = 5
GREEN_BLUE_LEDS        = 6
RED_GREEN_BLUE_LEDS    = 7
ALT_RED_GREEN_LEDS     = 8
ALT_AMBER_RED_LEDS     = 9
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2012
# -----------------------------------------------------------------------------
#        Timers.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in
#   Timers.c.
# -----------------------------------------------------------------------------
# =============================================================================
#  Time Values in 1 mS ticks
ONE_MINUTE                 = 60000
THIRTY_SECONDS             = 30000
ONE_SECOND                 = 1000
TWO_SECONDS                = 2000
THREE_SECONDS              = 3000
FOUR_SECONDS               = 4000
FIVE_SECONDS               = 5000
EIGHT_SECONDS              = 8000
TEN_SECONDS                = 10000
ELEVEN_SECONDS             = 11000
EIGHT_HUNDRED_MILLISECONDS  = 800
SEVEN_HUNDRED_MILLISECONDS  = 700
SIX_HUNDRED_MILLISECONDS   = 600
FIVE_HUNDRED_MILLISECONDS  = 500
FOUR_HUNDRED_MILLISECONDS  = 400
THREE_HUNDRED_MILLISECONDS  = 300
TWO_HUNDRED_MILLISECONDS   = 200
ONE_HUNDRED_MILLISECONDS   = 100
FIFTY_MILLISECONDS         = 50
SIXTY_MILLISECONDS         = 60
THIRTY_FIVE_MILLISECONDS   = 35
TWENTY_FIVE_MILLISECONDS   = 25
TWENTY_MILLISECONDS        = 20
TEN_MILLISECONDS           = 10
CARD_TRACKER_TIMER                = 0
RF_COUNT_DOWN_TIMER               = 1
FEATURE_COUNT_DOWN_TIMER          = 2
TAMPER_COUNT_DOWN_TIMER           = 3
BLE_COUNT_DOWN_TIMER              = 4
KP_POWER_SAVER_COUNT_DOWN_TIMER   = 5
OSDP_ACCESS_DATA_COUNTDOWN_TIMER  = 6
SELF_ENROLL_COUNT_DOWN            = 7
KP_IDLE_COUNT_DOWN_TIMER          = 8
BLE_AMBER_LED_COUNT_DOWN_TIMER    = 9
MCLP_LED_TIMER                    = 10
BLE_ALIVE_COUNT_DOWN_TIMER        = 11
BLINKING_LED_COUNT_DOWN_TIMER     = 12
DUAL_AUTH_COUNT_DOWN_TIMER        = 13
DM_VALID_FILE_COUNT_DOWN          = 14
F2F_POLL_COUNT_DOWN               = 15
F2F_OFF_LINE_COUNT_DOWN           = 16
F2F_TAMPER_COUNT_DOWN             = 17
F2F_ERROR_COUNT_DOWN_TIMER        = 18
PULSED_BEEPER_COUNT_DOWN_TIMER    = 19
PIV_COUNT_DOWN_TIMER              = 20
PIN_ENRTY_DURATION_TIMER          = 21
OSDP_ONLINE_COUNTDOWN_TIMER       = 22
LED_IDLE_COUNT_DOWN_TIMER         = 23
FILE_XFER_COUNTDOWN_TIMER         = 24
CAPTOUCH_TRIGGER_WINDOW_TIMER     = 25
CAPTOUCH_ANTI_PASSBACK_TIMER      = 26
CAPTOUCH_TEST_TIMER               = 27
MOBILE_TRANSACTION_TIMER          = 28
CAPTOUCH_INTERVAL_TIMER	          = 29
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        Wiegand.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in Wiegand.c
# -----------------------------------------------------------------------------
# =============================================================================
# 
#  Default Wiegand timing in uS.
# 
DEFAULT_WIEGAND_PULSE      = 100
DEFAULT_WIEGAND_SPACE      = 1000
FORMAT_RIGHT_JUSTIFY    = 0
FORMAT_LEFT_JUSTIFY     = 1
WIEGAND_DATA_SRC_KEY_PRESS		 = 0
WIEGAND_DATA_SRC_PROXIMITY_FSK	 = 1
WIEGAND_DATA_SRC_CAUSE_OF_RESET  = 2
WIEGAND_DATA_SRC_CSN             = 3
WIEGAND_DATA_SRC_NEXPACS         = 4
WIEGAND_DATA_SRC_MFD_SMARTMAX    = 5
WIEGAND_DATA_SRC_FIPS_201_1      = 6
WIEGAND_DATA_SRC_EYELOCK_TOC     = 7
WIEGAND_DATA_SRC_VISA_MFC_APP    = 8
WIEGAND_DATA_SRC_BLE             = 9
WIEGAND_DATA_SRC_LEAF_IP         = 10
WIEGAND_DATA_SRC_FW_INFO         = 11
WIEGAND_DATA_SRC_MFC_SMARTMAX    = 12
WIEGAND_DATA_SRC_MFC_FIDELITY    = 13
WIEGAND_DATA_SRC_MFD_FIDELITY    = 14
WIEGAND_DATA_SRC_PROXIMITY_ASK	 = 15
WIEGAND_DATA_SRC_DAIMLER_CID	 = 16
WIEGAND_DATA_SRC_UPS			 = 17
WIEGAND_DATA_SRC_BLE_CASI        = 18
WIEGAND_DATA_SRC_BARRY			 = 19
WIEGAND_DATA_SRC_NFC 			 = 20
WIEGAND_DATA_SRC_MORPHO_BIO_APP  = 21
WIEGAND_DATA_SRC_NFC_CASI        = 22
WIEGAND_DATA_SRC_OPEN_BCD        = 23
WIEGAND_DATA_SRC_MFC_SWH         = 24
WIEGAND_DATA_SRC_MFD_SWH         = 25
WIEGAND_DATA_SRC_MIFARE_2GO_LEAF      = 26
WIEGAND_DATA_SRC_MIFARE_2GO_GENERIC   = 27
WIEGAND_DATA_SRC_MFD_DORMA_KABA       = 28
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2015
# -----------------------------------------------------------------------------
#        HostInterface.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in HostInterface.c
# -----------------------------------------------------------------------------
# =============================================================================
HOST_BUF_SIZE        = MAX_OSDP_RX_LEN
HOST_WIEGAND_PROTOCOL        = 0
HOST_OSDP_PROTOCOL           = 1
HOST_TLV_PROTOCOL_OBSOLETE   = 2
HOST_MCLP_PROTOCOL           = 3
HOST_F2F_PROTOCOL            = 4
HOST_INT_BUF_SIZE       = 128
# HOST_CMD_STATE_ACQUIRE   0
# HOST_CMD_STATE_COMPLETE  1
# 
#  LED Colors
# 
LED_BLACK       = 0
LED_RED         = 1
LED_GREEN       = 2
LED_AMBER       = 3
# HOST_TEST_RUN_TESTS          0x90
# HOST_TEST_POLL_TESTS         0x91
HOST_TEST_SERIALIZE_READER    = 0x92
HOST_CLEAR_RESET_HISTORY      = 0x93
HOST_GET_RESET_HISTORY        = 0x94
HOST_SET_DF_NAME              = 0x95
HOST_TEST_WEIGAND             = 0x96
HOST_SET_CAP_THRESHOLD        = 0x97
HOST_GET_DEVICE_DESCRIPTION   = 0x98
HOST_TEST_PCB_ID              = 0x99
HOST_TEST_RDR_CONNECTED       = 0x9A
HOST_TEST_GET_SERIAL          = 0x9B
HOST_TEST_GET_SERIAL          = 0x9B
HOST_EXTENDED_READER_INFO     = 0x9C
CUSTOMER_LED                 = 0x41
CUSTOMER_BUZZER				 = 0x42
CUSTOMER_GLOBAL_BUZZER_ON		 = 0x01
CUSTOMER_CARD_AV_BUZZER_ON		 = 0x02
CUSTOMER_TECHNOLOGY			 = 0x43
CUSTOMER_TECH_LOW_FREQUENCY		 = 0x01
CUSTOMER_TECH_HIGH_FREQUENCY	 = 0x02
CUSTOMER_TECH_BLE				 = 0x04
CUSTOMER_CREDENTIALS         = 0x44
CUSTOMER_CREDENTIALS_EV1_EV2_CSN_ENABLE	 = 0x01
CUSTOMER_CREDENTIALS_MFC_CSN_ENABLE		 = 0x02
CUSTOMER_CREDENTIALS_ICLASS_CSN_ENABLE   = 0x04
CUSTOMER_CREDENTIALS_BLE_ENABLE		 = 0x10
CUSTOMER_CREDENTIALS_NFC_ENABLE		 = 0x20
CUSTOMER_CREDENTIALS_LEAF_ENABLE	 = 0x40
CUSTOMER_CREDENTIALS_ECP_ENABLE		 = 0x80
CUSTOMER_MOBILE						 = 0x45
CUSTOMER_ECP						 = 0x46
CUSTOMER_KEYS						 = 0x47
CUSTOMER_KEYS_LEAF_IP_OCPSK_KEYSET	 = 6
CUSTOMER_KEYS_LEAF_IP_READ_KEYSET	 = 7
CUSTOMER_KEYS_CUSTOMER_MEM           = 24
CUSTOMER_KEYS_NFC_KM1_KEYS           = 26
CUSTOMER_KEYS_NFC_KC1_KEYS           = 27
CUSTOMER_KEYS_NFC_KM2_KC2_KEYS       = 28
CUSTOMER_KEYS_NFC_KC2_KEYS           = 29
CUSTOMER_RTFD                = 0x48
CUSTOMER_OSDP						 = 0x49
CUSTOMER_TAMPER                      = 0x4a
MAX_OSDP_ADDRESS					 = 0x7E
#  Event Values
HOST_EVENT_TAMPER_ACTIVE            = 1
HOST_EVENT_TAMPER_INACTIVE          = 2
#  DEBUG print over RS-485
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2015
# -----------------------------------------------------------------------------
#        KeyPad.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in KeyPad.c
# -----------------------------------------------------------------------------
# =============================================================================
KEYPAD_BUF_SIZE       = 32
MAX_BUFFERED_26_BIT_KEYS     = 5
MAX_BUFFERED_KEYS            = 10
KP_FORMAT_4_BIT              = 0
KP_FORMAT_6_BIT              = 1
KP_FORMAT_8_BIT              = 2
KP_FORMAT_26_BIT             = 3
KP_FORMAT_BUFFERED_4_BIT     = 4
KP_FORMAT_ASCII              = 5
KP_FORMAT_MAGSTRIPE          = 6
KP_START_SENTINEL            = 0x0B
KP_DATA_SEPARATOR            = 0x0D
KP_END_SENTINEL              = 0x0F
KP_KEY_STAR             = 0x0A
KP_KEY_HASH_STD         = 0x0B
KP_KEY_HASH_F2F         = 0x0C
TLV_TAG_KEYPRESS                = 0x60
TLV_TAG_KEYPAD_LED              = 0x61
TLV_TAG_KEYPAD_INFO             = 0x62
TLV_TAG_KEYPAD_MAP_LED          = 0x63
ALL_KP_LEDS   = 0xFF
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        NexPacs.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in NexPacs.c
# -----------------------------------------------------------------------------
# =============================================================================
CIO_FILE        = 0x01
CDO_FILE        = 0x02
NEXPACS_AID_B0  = 0xF5
NEXPACS_AID_B1  = 0x32
NEXPACS_AID_B2  = 0xF0
NEXPACS_AID_B2_FA  = 0xFA
#  Used for Linxens Bio Card
NEXPACS_AID_B2_BIO  = 0xFA
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2016
# -----------------------------------------------------------------------------
#        osdp.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in osdp.c
# -----------------------------------------------------------------------------
# =============================================================================
#  WaveLynx Legacy Vendor Code
#  'W'
WL_LEGACY_VENDOR_CODE_1   = 0x57
#  'A'
WL_LEGACY_VENDOR_CODE_2   = 0x41
#  'V'
WL_LEGACY_VENDOR_CODE_3   = 0x56
#  Official IEEE assigned OID WaveLynx Vendor Code
WL_VENDOR_CODE_1   = 0x5C
WL_VENDOR_CODE_2   = 0x26
WL_VENDOR_CODE_3   = 0x23
#  INID Vendor Code
INID_VENDOR_CODE_1   = 0x00
INID_VENDOR_CODE_2   = 0x75
INID_VENDOR_CODE_3   = 0x32
OSDP_BROADCAST_ADDR        = 0x7F
# 
#  OSDP States
# 
OSDP_IDLE                = 0
OSDP_RECEIVING           = 1
OSDP_RECEIVE_COMPLETE    = 2
OSDP_BEGIN_TRANSMIT      = 4
OSDP_TRANSMIT_COMPLETE   = 5
# 
#  UART Setting Change States
# 
SP_STABLE     = 0
SP_CHANGED    = 1
DISABLED         = 0
ENABLED          = 1
#  OSDP message components
SOM_CHAR  = 0x53 #  Start Of Message
#  OSDP Commands
CMD_POLL 					 = 0x60
CMD_ID_REQ			 		 = 0x61
CMD_CAPABILTY_REQ			 = 0x62
CMD_DIAG_FUNC				 = 0x63  #  Not Supported */
CMD_LOCAL_STAT_REQ			 = 0x64
CMD_INPUT_STAT_REQ			 = 0x65  #  Not Supported */
CMD_OUTPUT_STAT_REQ			 = 0x66  #  Not Supported */
CMD_READER_STAT_REQ			 = 0x67  #  Not Supported */
CMD_OUTPUT_CNTRL			 = 0x68  #  Not Supported */
CMD_LED_CNTRL				 = 0x69
CMD_BUZ_CNTRL				 = 0x6A
CMD_TEXT_OUTPUT				 = 0x6B  #  Not Supported */
CMD_READER_MODE_CNTRL		 = 0x6C  #  Not Supported */
CMD_TIME_DATE				 = 0x6D  #  Not Supported */
CMD_COMSET					 = 0x6E
CMD_DATA_TRANSFER            = 0x6F
CMD_PROMPT                   = 0x71
CMD_BIO_READ                 = 0x73  #  Not Supported */
CMD_BIO_MATCH                = 0x74  #  Not Supported */
CMD_KEY_SET                  = 0x75
CMD_CHALLENGE                = 0x76
CMD_SERVER_CRYPTO            = 0x77
CMD_FILE_TRANSFER            = 0x7C
CMD_MFG_RESERVED			 = 0x80
CMD_ACURXSIZE				 = 0x7B
CMD_ABORT					 = 0xA2
CMD_PIVDATA					 = 0xA3
CMD_GENAUTH					 = 0xA4
CMD_CRAUTH					 = 0xA5
CMD_MFGSTAT					 = 0xA6
CMD_KEEP_ACTIVE				 = 0xA7
#  OSDP Responses
RSP_ACK						 = 0x40
RSP_NAK						 = 0x41
RSP_ID_REP					 = 0x45
RSP_CAPABILITY_REP			 = 0x46
RSP_LOCAL_STAT_REP			 = 0x48
RSP_INPUT_STAT_REP			 = 0x49
RSP_OUTPUT_STAT_REP			 = 0x4A
RSP_READER_STAT_REP			 = 0x4B
RSP_READER_DATA_RAW			 = 0x50
RSP_READER_DATA_FMT			 = 0x51
RSP_EXT_CARD_DATA			 = 0x52
RSP_KEYPAD_DATA				 = 0x53
RSP_COMM_CONFIG_REP			 = 0x54
RSP_CLIENT_CRYPTO            = 0x76
RSP_INITIAL_R_MAC            = 0x78
RSP_PD_BUSY                  = 0x79
RSP_FT_STAT                  = 0x7A
RSP_PIVDATAR                 = 0x80
RSP_GENAUTHR                 = 0x81
RSP_CRAUTHR                  = 0x82
RSP_MFGSTATR                 = 0x83
RSP_MFGERR                   = 0x84
RSP_MFG_RESERVED			 = 0x90
RSP_TBD_OR_NOT				 = 0x98
#  OSDP Message Index Values
OSDP_START					 = 0x00
OSDP_ADDR					 = 0x01
OSDP_LEN_LSB				 = 0x02
OSDP_LEN_MSB				 = 0x03
OSDP_CTL_STAT				 = 0x04
OSDP_CMD_REPLY				 = 0x05
OSDP_SEC_BLK_LEN             = 0x05
OSDP_SEC_BLK_TYPE            = 0x06
OSDP_SEC_BLK_DATA            = 0x07
OSDP_CARD_DATA_BITS_LSB		 = 0x08
OSDP_CARD_DATA_BITS_MSB		 = 0x09
OSDP_CARD_DATA_START		 = 0x0A
BUZ_CMD_LEN                  = 5
LED_CMD_LEN                  = 14
MAX_STACKED_COMMANDS         = 6
CMD_NOT_SUPPORTED			 = 0x0000
LED_PORT_MASK				 = 0xFF9F
CTRL_SBC_BIT                 = 0x08
CTRL_CKSUM_CRC_BIT           = 0x04
CTRL_SQN_MASK                = 0x03
OSDP_BR9600                  = 0
OSDP_BR14400                 = 1
OSDP_BR19200                 = 2
OSDP_BR28800                 = 3
OSDP_BR38400                 = 4
OSDP_BR57600                 = 5
OSDP_BR115200                = 6
OSDP_BR230400                = 7
OSDP_SCS_00                  = 0x00
OSDP_SCS_11                  = 0x11
OSDP_SCS_12                  = 0x12
OSDP_SCS_13                  = 0x13
OSDP_SCS_14                  = 0x14
OSDP_SCS_15                  = 0x15
OSDP_SCS_16                  = 0x16
OSDP_SCS_17                  = 0x17
OSDP_SCS_18                  = 0x18
OSDP_NO_ERROR                = 0x00
OSDP_BAD_CSUM_CRC            = 0x01
OSDP_CMD_LEN_ERROR           = 0x02
OSDP_UNKNOWN_CMD             = 0x03
OSDP_UNEXPECTED_SEQ_NUM      = 0x04
OSDP_UNSUPPORTED_SEC_BLK     = 0x05
OSDP_ENC_COM_EXPECTED        = 0x06
OSDP_BIO_TYPE_NOT_SUPPORTED  = 0x07
OSDP_BIO_FRMT_NOT_SUPPORTED  = 0x08
OSDP_UNABLE_TO_PROCESS       = 0x09
FC_CONTACT_STS_MON           = 0x01
FC_OUTPUT_CONTROL            = 0x02
FC_CARD_DATA_FORMAT          = 0x03
FC_LED_CONTROL               = 0x04
FC_AUDIBLE_OUTPUT            = 0x05
FC_TEXT_OUTPUT               = 0x06
FC_TIME_KEEPING              = 0x07
FC_CHK_CHAR_SUPPORT          = 0x08
FC_COMM_SECURITY             = 0x09
FC_RX_BUFFER_SIZE            = 0x0A
FC_MAX_MSG_SIZE              = 0x0B
FC_SMART_CARD_SUPPORT        = 0x0C
FC_READERS                   = 0x0D
FC_BIOMETRICS                = 0x0E
FC_SPE_SUPPORT               = 0x0F
FC_OSDP_VERSION              = 0x10
OSDP_LED_CMD_SIZE            = 20
OSDP_BUZZER_CMD_SIZE         = 12
OSDP_KEY_LEN_MAX             = 16
OSDP_RND_AB_LEN_MAX          = 8
OSDP_UID_LEN                 = 8
SCBK_D    = 0   #  Default Secure Channel base Key
SCBK      = 1   #  Active Secure Channel Base Key
# 
#  FT_STAT Response Field Values
# 
#  Stay in secure channel if active and allow interleaved OSDP traffic
FT_ACTION_INTERLEAVE_OK            = 0x01
FT_ACTION_SECURE_NOT_OK            = 0x02
FT_ACTION_ACCESS_DATA_AVAILABLE    = 0x04
FT_DELAY_NONE                      = 0
FT_STATUS_DETAIL_OK_TO_PROCEED     = 0
FT_STATUS_DETAIL_PROCESSED_OK      = 1
FT_STATUS_DETAIL_REBOOTING         = 2
FT_STATUS_DETAIL_NEED_PROCESSING   = 3
FT_STATUS_ABORT_TRANSFER           = (-1)
FT_STATUS_UNRECOGNIZED_FILE        = (-2)
FT_STATUS_UNACCEPTABLE_FILE        = (-3)
FT_UPDATE_MSG_MAX_NO_CHANGE        = 0
FT_FILE_TYPE_FIRMWARE              = 1
FT_FILE_TYPE_WL_CONFIG             = 0xFC
# 
#  Data Manager States
# 
DM_IDLE                   = 0
DM_READY_TO_PROCESS       = 1
DM_DATABASE               = 2
DM_VALIDATE_FILE          = 3
DM_VALIDATION_PASSED      = 4
# 
#  INID Extended Commands, replies, and codes
# 
#  Command Codes
inid_XTCMD         = 0xFF
inid_ABORT         = 0xFD
inid_GETPIVDATA    = 0x10
inid_GENAUTH       = 0x11
inid_CPRXSIZE      = 0x12
inid_KP_ACT        = 0x13
inid_CRAUTH        = 0x14
#  Reply Codes
inid_XTCMDRPLY     = 0xFF
inid_VERR          = 0xFE
inid_VSTAT         = 0xFD
inid_PIVDATARPLY   = 0x10
inid_GENAUTHRPLY   = 0x11
#  Error Codes
inid_SC_ERROR           = 0x01
inid_SC_TIMEOUT         = 0x02
inid_SC_NO_SUCH_FILE    = 0x03
#  Status Codes
inid_STAT_BUSY     = 0x01  #  UNUSED
inid_STAT_CONT     = 0x02
BR_9600           = 0
BR_19200          = 1
BR_38400          = 2
BR_57600          = 3
BR_115200         = 4
BR_230400         = 5
BR_460800         = 6
# 
#  Global functions defined in osdp.c
# 
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2020
# -----------------------------------------------------------------------------
#        ScEcpNfc.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in ScEcpNfc.c
# -----------------------------------------------------------------------------
# =============================================================================
VASUP_A                            = 0x6A
ECP_FORMAT_1                       = 0x01
ECP_FORMAT_2                       = 0x02
ECP_WL_TERMINAL_INFO_USER_AUTH     = 0x83
ECP_WL_TERMINAL_INFO               = 0xC3
ECP_TERMINAL_TYPE                  = 0x02
ECP_TERMINAL_SUBTYPE_UNIVERSITY    = 0x00
ECP_TERMINAL_SUBTYPE_CORPORATE     = 0x02
ECP_TERMINAL_SUBTYPE_HOSPITALITY   = 0x03
ECP_TERMINAL_SUBTYPE_RESIDENTIAL   = 0x04
ECP_TCI_1                          = 0x02
ECP_TCI_2_DEFAULT                  = 0x0D
ECP_TCI_3_DEFAULT                  = 0x03
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2023
# -----------------------------------------------------------------------------
#        DormaKaba.h
# -----------------------------------------------------------------------------
# 
#   This file contains declarations of functions defined in DormaKaba.c
# -----------------------------------------------------------------------------
# =============================================================================
# DORMA_KABA_H_
#  = 
# DORMA_KABA_AID_B0						 = 0xF5
# DORMA_KABA_AID_B1						 = 0x41
# DORMA_KABA_AID_B2						 = 0xD0
# DORMA_KABA_DESFIRE_FILE_NUM			     = 0
# DORMA_KABA_APP_DATA_LEN                 = 32
# DORMA_KABA_WIEGAND_BIT_LEN              = 80
# DORMA_KABA_WIEGAND_BYTE_LEN             = 10
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2023
# -----------------------------------------------------------------------------
#        DormaKaba.h
# -----------------------------------------------------------------------------
# 
#   This file contains declarations of functions defined in DormaKaba.c
# -----------------------------------------------------------------------------
# =============================================================================
DORMA_KABA_AID_B0						 = 0xF5
DORMA_KABA_AID_B1						 = 0x41
DORMA_KABA_AID_B2						 = 0xD0
DORMA_KABA_DESFIRE_FILE_NUM			     = 0
DORMA_KABA_APP_DATA_LEN                 = 32
DORMA_KABA_WIEGAND_BIT_LEN              = 80
DORMA_KABA_WIEGAND_BYTE_LEN             = 10
DORMA_KABA_START_BIT_LEN                = 24

# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2023
# -----------------------------------------------------------------------------
#        ACTPRO
# -----------------------------------------------------------------------------
# 
#   This file contains declarations of functions defined for ACTPRO
# -----------------------------------------------------------------------------
# =============================================================================
ACTPRO_AID_B0                           = 0xF5
ACTPRO_AID_B1                           = 0x16
ACTPRO_AID_B2                           = 0xC1
ACTPRO_DESFIRE_FILE_NUM                 = 1
ACTPRO_APP_DATA_LEN                     = 4
ACTPRO_WIEGAND_BIT_LEN                  = 37
ACTPRO_WIEGAND_BYTE_LEN                 = 5
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2014
# -----------------------------------------------------------------------------
#        CsnFormat.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in
#   CsnFormat.c.
# -----------------------------------------------------------------------------
# =============================================================================
CSN_AS_IS                = 0x00
CSN_4001                 = 0x01
CSN_4002                 = 0x02
CSN_5002                 = 0x03
CSN_6400                 = 0x04
CSN_26_BIT               = 0x05
CSN_32_BIT_LSB_XOR       = 0x06
CSN_32_BIT_MSB_XOR       = 0x07
CSN_40_BIT_MSB_LRC       = 0x08
CSN_34_BIT_MSB_PARITY    = 0x09
CSN_32_BIT_LSB           = 0x0A
CSN_32_BIT_MSB           = 0x0B
CSN_32_BIT_PLUS          = 0x0C
CSN_56_BIT               = 0x0D
CSN_40_BIT_PCSC          = 0x0E
CSN_75_BIT_PCSC          = 0x0F
CSN_5002_CL2             = 0x10
CSN_37_BIT               = 0x11
CSN_56_BIT_MSB           = 0x12
MAX_FORMATTED_CSN_LEN    = 15
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        BitStream.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in BitStream.c.
# -----------------------------------------------------------------------------
# =============================================================================
MAX_BS_LEN        = 32
BS_FILTER_HF            = 0x01
BS_FILTER_LF            = 0x02
BS_FILTER_BLE           = 0x04
BS_FILTER_CSN           = 0x08
#  Filter Functions
#  0x00:  equal to
#  0x40:  more than or equal to
#  0x80:  less than or equal to
#  0xC0:  not equal to
BS_FILTER_FUNC_MASK     = 0xC0
BS_FILTER_FUNC_EQ       = 0x00
BS_FILTER_FUNC_ME       = 0x40
BS_FILTER_FUNC_LE       = 0x80
BS_FILTER_FUNC_NE       = 0xC0
#  Filter Immunity Functions (Note: Only set in BnAppliedFilter)
#  00:  No immunity
#  01:  Immunity for NFC Wallet
#  02:  Immunity for LEAF
#  03:  Immunity for both NFC Wallet and Leaf
BS_FILTER_IMMUNITY_MASK     = 0x30
BS_FILTER_IMMUNITY_NFC      = 0x10
BS_FILTER_IMMUNITY_LEAF     = 0x20
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        SymmetricKeys.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in
#   SymmetricKeys.c.
# -----------------------------------------------------------------------------
# =============================================================================
DIV_ALGO_NONE                    = 0
DIV_ALGO_NXP_STD                 = 1
DIV_ALGO_OPS_OBSOLETE            = 2
DIV_ALGO_SMARTMAX_3DES           = 3
DIV_ALGO_SMARTMAX_DES            = 4
DIV_ALGO_UNUSED_5                = 5
DIV_ALGO_FIDELITY_MFC            = 6
MAX_DIV_DATA_LEN                 = 31
FEATURE_MANAGEMENT_KEYSET           = 0
USER_APP_OCPSK_READ_KEYSET          = 1
USER_APP_CARD_MASTER_WRITE_KEYSET   = 2
EXT_MEM_OSDP_KEYSET                 = 3
BLE_MFC_KEYSET                      = 4
USER_APP2_K1_K2_KEYSET              = 5
LEAF_IP_OCPSK_READ_KEYSET           = 6
LEAF_IP_CARD_MASTER_WRITE_KEYSET    = 7
LEAF_IP_KS1_OCPSK_READ_KEYSET       = 8
LEAF_IP_KS2_OCPSK_READ_KEYSET       = 9
LEAF_IP_KS3_OCPSK_READ_KEYSET       = 10
M2G_ACD_LEAF_GENERIC_KEYS           = 11
CUSTOMER_EXT_MEM                    = 12
NFC_KM1_KC1_KEYS                    = 13
NFC_KM2_KC2_KEYS                    = 14
NFC_MP0_MC0_KEYS                    = 15
END_OF_STD_KEYSETS                  = 16
TRANSPORT_KEYSET                 = 0xFF
MAD_KEYSET                       = 0xFE
KEY1_OFFSET_AES128              = 0
KEY2_OFFSET_AES128              = 16
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2013
# -----------------------------------------------------------------------------
#        tlv.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in tlv.c
# -----------------------------------------------------------------------------
# =============================================================================
# 
#  General Tag Values
# 
TLV_TAG_ACK                     = 0x06
TLV_TAG_NAK                     = 0x16
TLV_TAG_CUST_CONFIG             = 0x0B
TLV_TAG_CONFIG                  = 0x0C
TLV_TAG_PRIORITY_ENVELOPE       = 0x0D
TLV_TAG_ENVELOPE                = 0x0E
TLV_TAG_FIRMWARE                = 0x0F
TLV_TAG_FIRMWARE_1_5            = 0x1F
TLV_TAG_BLE_CONFIG              = 0x1C
TVL_BLE_FCC_TEST_MODE           = 0x2B
# 
#  Feature Management Tag Values
# 
TLV_TAG_RESET_TO_STD_FEATURES      = 0xF0
TLV_TAG_FULL_FEATURE_SETUP         = 0xF1
TLV_TAG_UNUSED_F2                  = 0xF2
TLV_TAG_OPTION_SETTINGS            = 0xF3
TLV_TAG_RF_PROTOCOLS               = 0xF4
TLV_TAG_CARD_APPS                  = 0xF5
TLV_TAG_KEY_SET                    = 0xF6
TLV_TAG_KEY_PAD_MAP                = 0xF7
TLV_TAG_RESET_TO_STD_KEYS          = 0xF8
TLV_TAG_BLE_FOB_PAIRING            = 0xF9
TLV_TAG_BLE_AD_NAME                = 0xFA
TLV_TAG_RESET_TO_LOADED_CONFIG     = 0xFB
TLV_TAG_BIT_STREAM_FILTER          = 0xFC
TLV_TAG_ROTATE_OPTION              = 0xFD
TLV_TAG_FCC_TEST                   = 0xFE
TAG_UNIFIED_CONFIG_ENVELOPE   = 0xDE
TAG_UNIFIED_JOB_ID            = 0xDF
TLV_INVALID                        = 0xFF
# 
#  Misc. Tag Values
# 
TLV_TAG_ENVELOPE_CRC            = 0xEF
TLV_TAG_FW_VERSION              = 0xEE
TLV_TAG_KEY_SET_CRC             = 0xED
TLV_TAG_SETUP_DEV_DEBUG         = 0xEC
TLV_TAG_FORCE_SW_RESET          = 0xEB
TLV_TAG_HW_VERSION              = 0xEA
TLV_TAG_PASS_THRU_WITH_TO       = 0xE9
TLV_TAG_PASS_THRU_WITH_NO_TO    = 0xE8
TLV_TAG_SHADOW_CARD             = 0xE7
TLV_TAG_BLANK_SHADOW_CARD       = 0xE6
TLV_TAG_UNUSED_E5               = 0xE5
TLV_TAG_FORCE_WD_RESET          = 0xE4
TLV_TAG_TRANSMIT_FW_INFO        = 0xE3
TLV_TAG_CHANGE_RDR_SN           = 0xE2
TLV_USB_FULL_FEATURE_SETUP      = 0xD1
TLV_ECP_NFC_SETUP               = 0xD2
TLV_ANDROID_NFC_SETUP           = 0xD3
# 
#  Bit Stream Tag Values
# 
TLV_TAG_BS_DEFINITION           = 0xB0
TLV_TAG_BS_FORMAT               = 0xB1
TLV_TAG_BS_BID_MAP              = 0xB2
TLV_TAG_BS_FAC_MAP              = 0xB3
TLV_TAG_BS_ISS_MAP              = 0xB4
TLV_TAG_BS_PID_MAP              = 0xB5
TLV_TAG_BS_ORDER_NUM_MAP        = 0xB6
TLV_TAG_BS_CLEAR_BITS_MAP       = 0xB7
TLV_TAG_BS_SET_BITS_MAP         = 0xB8
TLV_TAG_BS_PARITY_MAP           = 0xB9
TLV_TAG_BS_CHECKSUM_MAP         = 0xBA
TLV_TAG_BS_ALGO                 = 0xBB
# 
#  Card Application Tag Values (Factory Programmer Only)
# 
#  Standard 37 bit FSK Proximity Card
TLV_TAG_CA_PROX_FSK             = 0xC0
#  NexPACS on Mifare DESFire Ev1
TLV_TAG_CA_NP_EV1               = 0xC1
#  Config Card App on Mifare DESFire Ev1
TLV_TAG_CA_CF_EV1               = 0xC2
#  EYELOCK Template On Card App on Mifare DESFire Ev1
TLV_TAG_CA_EL_EV1               = 0xC3
#  Formerly PROXESS Network On Card App on Mifare DESFire Ev1
TLV_TAG_CA_UNUSED_C4            = 0xC4
#  Leaf IP App on Mifare DESFire Ev2
TLV_TAG_CA_CC_EV2               = 0xC5
#  Isonas 60 bit FSK Proximity Card
TLV_TAG_CA_ISONAS_FSK           = 0xC6
#  Isonas 56 bit FSK Proximity Card
TLV_TAG_CA_ISONAS_LEAF_IP_FSK   = 0xC7
#  Leaf IP App on Mifare DESFire Ev2 with alternate bit stream
TLV_TAG_CA_CC_ALT_BS_EV2        = 0xC8
#  Recover EV1 Card
TLV_TAG_CA_RC_EV1               = 0xCE
#  Format EV1 Card
TLV_TAG_CA_FC_EV1               = 0xCF
# =============================================================================
#        WaveLynx Technologies Corporation Copyright (c) 2012
# -----------------------------------------------------------------------------
#        Fips201.h
# -----------------------------------------------------------------------------
# 
#   This file contains definitions for functions defined in Fips201.c
# -----------------------------------------------------------------------------
# =============================================================================
# 
#  Maximum number of KEEP_ACTIVE commands from the host that can be
#  dropped before the reader deactivates the extended RF function.
# 
MAX_KP_ACT_DROPPED      = 1
# 
#  FIPS-201-1 application command lengths
# 
SELECT_ENDPOINT_LEN        = 15
GET_DATA_LEN               = 11
GET_RESPONSE_LEN           = 5
# 
#  CHUID Tag Values
# 
DATA_OBJ_TAG     = 0x53
FASCN_TAG        = 0x30
GUID_TAG         = 0x34
EXP_DATE_TAG     = 0x35
FASCN_LEN             = 25
FORMATTED_FASCN_LEN   = 16
BCD_FASCN_LEN         = 40
GUID_LEN              = 16
EXP_DATE_LEN          = 8
# 
#  GUID Output Formats
# 
GUID_ALL         = 0x00
GUID_SENTINEL    = 0x01
# 
#  BCD FASC-N Field Indexes
# 
AGENCY_CODE_INDEX           = 1
SYSTEM_CODE_INDEX           = 6
CRED_NUM_INDEX              = 11
CRED_SERIES_INDEX           = 18
IND_CRED_ISSUE_INDEX        = 20
PERSON_ID_INDEX             = 22
ORG_CATEGORY_INDEX          = 32
ORG_ID_INDEX                = 33
POA_CATEGORY_INDEX          = 37
LRC_INDEX                   = 39
CHUID_OBJECT_ID_1         = 0x5F
CHUID_OBJECT_ID_2         = 0xC1
CHUID_OBJECT_ID_3         = 0x02
X509_CA_OBJECT_ID_1       = 0x5F
X509_CA_OBJECT_ID_2       = 0xC1
X509_CA_OBJECT_ID_3       = 0x01
CERTIFICATE_ELEMENT       = 0x70
# 
#  PIV Output Data Formats
# 
#   Notes:  TM means transaction status message include
#           CS means Credential Series
#           ISI means Individual Series Issue
# 
PIV_75_BIT_FORMAT           = 1
PIV_58_BIT_FORMAT           = 2
PIV_200_BIT_FORMAT          = 3
PIV_64_BIT_FORMAT           = 4
PIV_83_BIT_FORMAT           = 5
PIV_66_TM_FORMAT            = 6
PIV_64_TM_FORMAT            = 7
PIV_91_TM_FORMAT            = 8
PIV_40_BIT_BCD_FORMAT       = 9
PIV_40_BIT_REV_BCD_FORMAT   = 10
PIV_64_BIT_BCD_FORMAT       = 11
PIV_64_BIT_REV_BCD_FORMAT   = 12
PIV_128_BIT_BCD_FORMAT      = 13
PIV_128_BIT_REV_BCD_FORMAT  = 14
PIV_58_BIT_HSE_FORMAT       = 15
FIPS_201_IDLE                = 0
FIPS_201_ERROR               = 1
FIPS_201_BUSY                = 2
FIPS_201_CONTINUE            = 3
FIPS_201_PIVDATA_AVAILABLE   = 4
FIPS_201_CR_AVAILABLE        = 5
FIPS_MAX_DATA_SIZE           = 384
PIV_CARD_DATA_MAX_SIZE       = 384
#  PIV  Encryption Algorithms
RSA_CODE                         = 0x07
ECC_CURVE_256                    = 0x11
ECC_CURVE_384                    = 0x14
#  PIV Authentication Keys
CARD_AUTH_KEY              = 0x9E
PIV_AUTH_KEY               = 0x9A
#  SP800-73-3, Section 3.2.4, Table 6
DYNAMIC_AUTHENTICATION_TAG     = 0x7C
RESPONSE_TO_CHALLENGE_TAG      = 0x82
# 
#  Global functions defined in Fips201.c
# 
