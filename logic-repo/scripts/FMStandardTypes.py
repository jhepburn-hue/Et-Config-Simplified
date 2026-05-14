import struct
import features as wl
import warnings
import sys

# import crcmod


class TAG_OPTION:
    def __init__(self):
        # see wl.BIT_OP_CLEAR,SET,TOGGLE
        # 0 sets the whole word but there is no define for that operation
        self.operation = 0
        self.index = 0
        self.value = 0

    # see wl.BIT_OP_CLEAR,SET,TOGGLE
    # 0 sets the whole word but there is no define for that operation
    def set(self, operation, index, value):
        self.operation = operation
        self.index = index
        self.value = value

    def __mkU8bytes(self, value):
        return value.to_bytes(1, byteorder="little", signed=False)

    def __mkU16bytes(self, value):
        return value.to_bytes(2, byteorder="big", signed=False)

    def dumpTlv(self):
        final = (
            self.__mkU8bytes(wl.TLV_TAG_OPTION_SETTINGS)
            + self.__mkU8bytes(4)
            + self.__mkU8bytes(self.operation)
            + self.__mkU8bytes(self.index)
            + self.__mkU16bytes(self.value)
        )
        return final


class RfProtocolsConfig:
    """
    Helper class for constructing the config TLV to set or change the RF protocols
    supported by the reader for HF cards.

    The RF protocols TLV is simply a straight list of protocol IDs which will
    overwrite those configured in the reader wholly. Only 16 protocols can be supported
    at one time.
    """

    def __init__(self):
        """
        Simply init the list of RF protocols.
        """
        self.protocols: bytearray = bytearray([])

    def append_protocol(self, protocol: int):
        """
        Append an RF protocol to the list. This function will raise an
        exception if a valid protocol is not provided or if the max number
        of protocols have been exceeded.

        Params:
            protocol: Protocol ID to append.
        """
        if (protocol < wl.CP_NONE) or (protocol > wl.CP_FELICA):
            raise Exception("Provided RF protocol out of valid range")

        if (len(self.protocols) + 1) > wl.MAX_PROTOCOLS:
            raise Exception("Max supported RF protocols exceeded")

        self.protocols = self.protocols + bytearray([protocol])

    def dump_tlv(self) -> bytes:
        """
        Dump the serialized config TLV for the current RF protocol.

        [F4][LEN][PROTOCOLS ... ]

        Returns:
            Serialized TLV.
        """
        return bytes([wl.TLV_TAG_RF_PROTOCOLS, len(self.protocols)]) + self.protocols


class CardAppsConfig:
    """
    Helper class for constructing the config TLV for setting the card applications
    supported by the reader.

    The card apps TLV contains the card type as the first index of the value field

    The rest of the value field contains a list of supported card app IDs, which
    will overwrite the existing values in the reader wholly.
    """

    def __init__(self):
        self.card_apps: bytearray = bytearray([])
        self.card_type: int = -1

    def set_card_type(self, card_type: int):
        """
        Set the desired card type to apply the list of card apps to.

        Params:
            - card_type: Card type to overwrite apps for.
        """
        if (card_type < 0) or (card_type > wl.MAX_VALID_CARD_TYPES):
            raise Exception("invalid card type set for card apps config")

        self.card_type = card_type

    def append_card_app(self, app: int):
        """
        Append a card app ID to the card app list.

        Params:
            - app: Card app ID.
        """
        # this is a very crude check, as the card app IDs are not fully contiguous
        if (app > wl.CA_M2GO_GENERIC_ACD) or (app < 0):
            raise Exception("invalid card app id provided")

        if (len(self.card_apps) + 1) > wl.MAX_CARD_APPS:
            raise Exception("maximum card apps for single card type exceeded")

        self.card_apps = self.card_apps + bytearray([app])

    def dump_tlv(self) -> bytes:
        """
        Dump the serialized config TLV for setting the card apps for the given
        card type.

        [F5][LEN][CARD TYPE][CARD APPS ...]

        Returns:
            Serialized TLV bytes.
        """
        return bytes([wl.TLV_TAG_CARD_APPS, len(self.card_apps), self.card_type]) + self.card_apps


class NFC_CONFIG:
    def __init__(self):
        self.features = wl.NFC_FEA_TRANSPORT
        self.activeKeysets = wl.NFC_FEA_TRANSPORT | wl.MOBILE_ACTIVE_KEYSET_SLOT2
        self.metadata = ""
        # Set up the default ECP NFC Configuration here.
        self.ecpFormat = wl.ECP_FORMAT_2
        self.ecpTerminalInfoMode = 0xC1
        self.ecpTerminalType = 0x01
        self.ecpTerminalSubType = 0x02
        self.ecpTCI_1 = 0x11
        self.ecpTCI_2 = 0x00
        self.ecpTCI_3 = 0x00
        self.ecpBitCount = 40
        self.ecpAppOptions = wl.DIVERSIFY_MC0_MASK

        self.rfu = bytearray(32)

    def mask(self, option, value):
        if "features" == option:
            self.features &= value
        if "activeKeysets" == option:
            self.activeKeysets &= value
        if "metadata" == option:
            self.metadata &= value
        if "ecpFormat" == option:
            self.ecpFormat &= value
        if "ecpTerminalInfoMode" == option:
            self.ecpTerminalInfoMode &= value
        if "ecpTerminalType" == option:
            self.ecpTerminalType &= value
        if "ecpTerminalSubType" == option:
            self.ecpTerminalSubType &= value
        if "ecpTCI_1" == option:
            self.ecpTCI_1 &= value
        if "ecpTCI_2" == option:
            self.ecpTCI_2 &= value
        if "ecpTCI_3" == option:
            self.ecpTCI_3 &= value
        if "ecpBitCount" == option:
            self.ecpBitCount &= value
        if "ecpAppOptions" == option:
            self.ecpAppOptions &= value

    def aug(self, option, value):
        if "features" == option:
            self.features |= value
        if "activeKeysets" == option:
            self.activeKeysets |= value
        if "metadata" == option:
            self.metadata |= value
        if "ecpFormat" == option:
            self.ecpFormat |= value
        if "ecpTerminalInfoMode" == option:
            self.ecpTerminalInfoMode |= value
        if "ecpTerminalType" == option:
            self.ecpTerminalType |= value
        if "ecpTerminalSubType" == option:
            self.ecpTerminalSubType |= value
        if "ecpTCI_1" == option:
            self.ecpTCI_1 |= value
        if "ecpTCI_2" == option:
            self.ecpTCI_2 |= value
        if "ecpTCI_3" == option:
            self.ecpTCI_3 |= value
        if "ecpBitCount" == option:
            self.ecpBitCount |= value
        if "ecpAppOptions" == option:
            self.ecpAppOptions |= value

    def set(self, option, value):
        if "features" == option:
            self.features = value
        if "activeKeysets" == option:
            self.activeKeysets = value
        if "metadata" == option:
            self.metadata = value
        if "ecpFormat" == option:
            self.ecpFormat = value
        if "ecpTerminalInfoMode" == option:
            self.ecpTerminalInfoMode = value
        if "ecpTerminalType" == option:
            self.ecpTerminalType = value
        if "ecpTerminalSubType" == option:
            self.ecpTerminalSubType = value
        if "ecpTCI_1" == option:
            self.ecpTCI_1 = value
        if "ecpTCI_2" == option:
            self.ecpTCI_2 = value
        if "ecpTCI_3" == option:
            self.ecpTCI_3 = value
        if "ecpBitCount" == option:
            self.ecpBitCount = value
        if "ecpAppOptions" == option:
            self.ecpAppOptions = value

    def __mkU8bytes(self, value):
        return value.to_bytes(1, byteorder="little", signed=False)

    def dump(self):
        final = (
            self.__mkU8bytes(self.features)
            + self.__mkU8bytes(self.activeKeysets)
            + self.metadata.ljust(wl.NFC_META_DATA_SIZE, "\0").encode("ascii")
        )
        final += (
            self.__mkU8bytes(self.ecpFormat)
            + self.__mkU8bytes(self.ecpTerminalInfoMode)
            + self.__mkU8bytes(self.ecpTerminalType)
            + self.__mkU8bytes(self.ecpTerminalSubType)
        )
        final += (
            self.__mkU8bytes(self.ecpTCI_1)
            + self.__mkU8bytes(self.ecpTCI_2)
            + self.__mkU8bytes(self.ecpTCI_3)
        )
        final += self.__mkU8bytes(self.ecpBitCount) + self.__mkU8bytes(self.ecpAppOptions)
        final += self.rfu
        return final

    def dumpTlv(self):
        final = (
            self.__mkU8bytes(wl.TLV_ECP_NFC_SETUP)
            + self.__mkU8bytes(wl.NFC_CONFIG_SIZE)
            + self.dump()
        )
        return final


class system_features:
    def __validOpt(self, optName, optValue):
        if optName > wl.MAX_OPTION_SETTINGS:
            sys.exit(
                "Error! option name ",
                optName,
                " is greater than ",
                wl.MAX_OPTION_SETTINGS,
            )
        if optValue > 0xFFFF:
            sys.exit("Error! option value ", optValue, " is greater than ", 0xFFFF)
        # I don't think this rule is needed on Current Hardware and is it this tools job to detect misconfigurations?
        #  if (
        #     (optName == wl.OPERATION_INDEX)
        #     and (optValue == wl.ENABLE_ASK_RF)
        #     and (self.fAskHwSupport is not True)
        # ):
        #     sys.exit("Error HW doesn't support ASK")
        # if ((optName == wl.OPERATION_INDEX) and ((optValue == wl.ENABLE_ASK_RF) or (optValue == wl.ENABLE_FSK_RF)) and ((int(self.type) & 0x1) != 0x1)):
        #     #sys.exit("Error platform doesn't support Low Frequency")
        #     return False
        return True

    def setOpt(self, optName, optValue):
        if self.__validOpt(optName, optValue):
            self.OpSettings[optName] = optValue
            return True
        return False

    def maskOutOpt(self, optName, optValue):
        if self.__validOpt(optName, optValue):
            self.OpSettings[optName] &= ~optValue
            return True
        return False

    # append the value to the option
    def appendOpt(self, optName, optValue):
        if self.__validOpt(optName, optValue):
            self.OpSettings[optName] |= optValue
            return True
        return False

    def maskOpt(self, optName, optValue):
        if self.__validOpt(optName, optValue):
            self.OpSettings[optName] &= optValue
            return True
        return False

    def clearOpt(self, optName):
        self.OpSettings[optName] = 0

    def setBS(self, bsName, bsValue):
        if bsName == "FILTER":
            self.BsAppliedFilter = bsValue
        if bsName == "NUM_BITS":
            self.BsNumBits = bsValue

    def augBS(self, bsName, bsValue):
        if bsName == "FILTER":
            self.BsAppliedFilter |= bsValue
        if bsName == "NUM_BITS":
            self.BsNumBits |= bsValue

    # set a Supported Card RF Protocols
    def setRf(self, entry, protocolVal):
        self.RfProtocols[entry] = protocolVal           # appended to finalBin in dump

    def setCardTypeApp(self, cardType, applicationNumber, application):
        self.CardTypesApps[cardType][applicationNumber] = application

    def clearCardTypeApp(self):
        for i in range(wl.MAX_CARD_TYPES):
            for j in range(wl.MAX_CARD_APPS):
                self.CardTypesApps[i][j] = wl.CA_NONE

    def setAllCardTypeApp(self, cardApp):
        for i in range(wl.MAX_CARD_TYPES):
            for j in range(wl.MAX_CARD_APPS):
                self.CardTypesApps[i][j] = cardApp      #CardTypesApp gets appended to finalBin in dump

    def setVersion(self, major, minor, build):
        if (
            (self.MainFwMajorVersion != major)
            or (self.MainFwMinorVersion != minor)
            or (self.MainFwBuildNumber != build)
        ):
            warnings.warn("Overriding Firmware version")
        self.MainFwMajorVersion = major
        self.MainFwMinorVersion = minor
        self.MainFwBuildNumber = build

    def setBleName(self, name):
        self.BleAdName = name

    def __mkU8bytes(self, value):
        return value.to_bytes(1, byteorder="little", signed=False)

    def dump(self):
        if self.type == 0:
            sys.exit("Missing hw variant")
        encodedOpSettings = struct.pack("<{}H".format(len(self.OpSettings)), *self.OpSettings)
        BleAdNameLen = bytearray(1)
        BleAdNameLen[0] = len(self.BleAdName)
        finalBin = encodedOpSettings
        # add in keypad and BLE
        finalBin += (
            self.KeyPadMap
            + self.__mkU8bytes(len(self.BleAdName))
            + self.BleAdName.ljust(8, "\0").encode("ascii")
        )

        # add in FW_VERSION
        fw_version = (
            self.__mkU8bytes(self.MainFwMajorVersion)
            + self.__mkU8bytes(self.MainFwMinorVersion)
            + self.__mkU8bytes(self.MainFwBuildNumber)
        )
        finalBin += fw_version
        # Bit stream filter
        # bsFilterInfo = self.__mkU8bytes(self.BsAppliedFilter) + self.__mkU8bytes(self.BsNumBits) + self.BsFilterMask.ljust(wl.FILTER_MAX_BYTE_SIZE, "\0").encode(
        #     "ascii"
        # ) + self.BsFilterValue.ljust(wl.FILTER_MAX_BYTE_SIZE, "\0").encode("ascii")
        bsFilterInfo = (
            self.__mkU8bytes(self.BsAppliedFilter)
            + self.__mkU8bytes(self.BsNumBits)
            + self.BsFilterMask
            + self.BsFilterValue
        )
        finalBin += bsFilterInfo

        finalBin += self.__mkU8bytes(self.MainFwReleaseCandidate)

        finalBin += self.nfcConfig.dump()
        finalBin += self.RfProtocols
        for cardType in range(wl.MAX_CARD_TYPES):
            finalBin += bytes(self.CardTypesApps[cardType])
        finalBin += self.rfu_1

        # for now ommit the keys add them in on Sequoia
        # for secKeySet in range(wl.MAX_KEY_SETS):
        #     finalBin += self.SecurityKeySets[secKeySet].ljust(wl.KEY_SET_SIZE, "\0").encode("ascii")

        # finalBin += self.GuardianKey.ljust(wl.AES_128_KEY_SIZE, "\0").encode("ascii")
        # newfile = open("pyTest.bin", "wb")
        # newfile.write(finalBin)
        return finalBin

    def disableAskSupport(self):
        self.__setAskHW_support(False)

    def enableAskSupport(self):
        self.__setAskHW_support(True)

    def __setAskHW_support(self, state):
        self.fAskHwSupport = state

    def __setDefaultOpSettings(self):
        # must match Features.c:setStdFeatureSet
        # Default LED operations
        #  Red LED On is idle state
        #  Green blink on card reads
        #  Blue LED PWM = 50% (5)
        #  Green LED PWM = 50% (5)
        #  Red LED PWM = 60% (6)
        #
        self.OpSettings[wl.LED_OPTIONS_1_INDEX] = 0x5560 | wl.RED_GREEN_LEDS | (wl.BLACK_LED << 2)

        #
        # Reader Sensitivity Settings
        #
        self.OpSettings[wl.SENSITIVITY_INDEX] = 0x0014  # OSDP Late Response = 20 * 10 = 200 mS
        self.OpSettings[wl.SENSITIVITY_INDEX] |= 0x0F00  # Accelerometer Sensitivity
        self.OpSettings[wl.SENSITIVITY_INDEX] |= 0xC000  # AS3911 HF Gain

        #
        # Default Card Tracker Timeout
        #
        self.OpSettings[wl.CARD_TRACKER_TIME_OUT_INDEX] = wl.ONE_SECOND

        #
        # Default Wiegand Timing
        #
        self.OpSettings[wl.WIEGAND_SPACE_INDEX] = wl.DEFAULT_WIEGAND_SPACE
        self.OpSettings[wl.WIEGAND_PULSE_INDEX] = wl.DEFAULT_WIEGAND_PULSE

        #
        # Default Tamper Report Condition
        #
        self.OpSettings[wl.OPERATION_INDEX] |= wl.REPORT_TAMPER_STATE_CHANGE_ONLY
        # OSDP settings
        self.OpSettings[wl.HOST_SP_OPTIONS_INDEX] = wl.BR_9600
        i = wl.HOST_OSDP_PROTOCOL << 10
        self.OpSettings[wl.HOST_SP_OPTIONS_INDEX] &= ~(wl.HOST_SP_PROTOCOL_MASK)
        self.OpSettings[wl.HOST_SP_OPTIONS_INDEX] |= i

        #
        # Enable Host Interface as auto-detect OSDP/Wiegand
        # Enable RS-485, OSDP, and ASCII key press output. Default baud rate = 9600
        # LEDs on in idle state, inactive key LEDS blink off on key press,
        # and beep with each key press.
        #

        self.OpSettings[wl.OPERATION_INDEX] |= wl.OSDP_AUTO_DETECT_ACTIVE

        self.OpSettings[wl.EXT_OPERATION_INDEX] |= wl.TAMPER_INITIATES_OSDP_AUTO

        self.OpSettings[wl.OSDP_KP_OPTIONS_INDEX] = (
            wl.KP_FORMAT_ASCII
            | wl.KEYPAD_BEEP_ACTIVE_MASK
            | wl.KEYPAD_LED_IDLE_MASK
            | wl.KEYPAD_LED_ACTIVE_MASK
            | wl.KEYPAD_LED_INVERT_MASK
        )

        #
        # Setup the non-OSDP reader default key pad press to 8 bit format,
        # LEDs on in idle state, inactive key LEDS blink off on key press,
        # and beep with each key press.
        #
        self.OpSettings[wl.KEYPAD_OPTIONS_INDEX] = (
            wl.KP_FORMAT_8_BIT
            | wl.KEYPAD_BEEP_ACTIVE_MASK
            | wl.KEYPAD_LED_IDLE_MASK
            | wl.KEYPAD_LED_ACTIVE_MASK
            | wl.KEYPAD_LED_INVERT_MASK
        )
        #
        # Setup BLE Uart Baud Rate and Physical Access app mode
        # Bootloading and config file loading can occur with no timeout.
        # BLE AV overrides OSDP AV.
        #
        self.OpSettings[wl.BLE_OPTIONS_1_INDEX] = wl.BR_57600
        i = wl.BLE_PAC_DEVICE_UID << 4
        self.OpSettings[wl.BLE_OPTIONS_1_INDEX] |= i
        self.OpSettings[wl.BLE_OPTIONS_1_INDEX] |= wl.BLE_ALLOW_BOOT_LOAD_MASK
        self.OpSettings[wl.BLE_OPTIONS_1_INDEX] |= wl.BLE_OVERRIDE_OSDP_AV_MASK
        self.OpSettings[wl.BLE_TIMEOUT_MSW_INDEX] = wl.BLE_DEFAULT_TIMEOUT >> 16
        self.OpSettings[wl.BLE_TIMEOUT_LSW_INDEX] = wl.BLE_DEFAULT_TIMEOUT & 0x0000FFFF

        #
        # Set up all default NexPACS options
        #
        self.OpSettings[wl.NEXPACS_OPTIONS_INDEX] = wl.SKIP_CIO
        i = wl.NEXPACS_AID_B2 << 8
        i |= wl.NEXPACS_AID_B1
        self.OpSettings[wl.NEXPACS_APP_SETTINGS_1_INDEX] = i
        i = wl.NEXPACS_AID_B0 << 8
        self.OpSettings[wl.NEXPACS_APP_SETTINGS_2_INDEX] = i

        self.OpSettings[wl.CARD_DATA_FORMAT_INDEX] = (
            wl.CARD_DATA_FULL_BIT_STREAM | wl.CARD_DATA_HEXIDECIMAL
        )

        #
        # Default LEAF Si - Kv1 - App1 AID - Access File A (2) - EV1_CARD_KEY_1
        # Ignore custom key sets.
        #
        self.OpSettings[wl.LEAF_IP_DEF_INDEX] = 1
        self.OpSettings[wl.LEAF_IP_KS1_INDEX] = wl.LEAF_IP_IGNORE_KEYSET_MASK
        self.OpSettings[wl.LEAF_IP_KS2_INDEX] = wl.LEAF_IP_IGNORE_KEYSET_MASK
        self.OpSettings[wl.LEAF_IP_KS3_INDEX] = wl.LEAF_IP_IGNORE_KEYSET_MASK

        # BLE connection AV setup = solid Amber LED
        self.OpSettings[wl.BUILD_INDEX] |= 0x3000  # 3 * 50 = 150 mS period
        self.OpSettings[wl.BUILD_INDEX] |= 0x0300  # AMBER LED

        # Set up optional FIPS processing for INID protocol
        self.OpSettings[wl.FIPS_201_INDEX] |= wl.FIPS_201_USE_VSTAT_REPLY

        # Set default OSDP Vendor Code
        self.OpSettings[wl.OSDP_VENDOR_CODE_VC1_INDEX] = wl.WL_VENDOR_CODE_1
        self.OpSettings[wl.OSDP_VENDOR_CODE_VC2_3_INDEX] = (
            wl.WL_VENDOR_CODE_2 << 8
        ) | wl.WL_VENDOR_CODE_3

        # Allow stacked OSDP AV commands.
        self.OpSettings[wl.LED_OPTIONS_2_INDEX] |= wl.ALLOW_STACKED_OSDP_AV_CMDS_MASK

        # Right justify AWID FSK bit streams.
        self.OpSettings[wl.PROX_BITSTREAM_FORMAT] |= wl.PROX_RIGHT_JUSTIFY_AWID_MASK

        self.OpSettings[wl.RF_POLL_TIMEOUT] = wl.SIXTY_MILLISECONDS
        # Enable special features
        self.OpSettings[wl.SPECIAL_FEATURES_INDEX] = 0
        # self.OpSettings[wl.SPECIAL_FEATURES_INDEX] |= wl.LEAF_IP_SKIP_HS_FILE_MASK
        self.OpSettings[wl.SPECIAL_FEATURES_INDEX] |= wl.LEAF_IP_SKIP_SIG_MASK
        self.OpSettings[wl.SPECIAL_FEATURES_INDEX] |= wl.ENABLE_EXCLUSIVE_HOST_LOAD

        # SIGMA DELTA TAMPER
        self.OpSettings[wl.ACCEL_TAMPER_SIGMA] = 0
        self.OpSettings[wl.ACCEL_TAMPER_SIGMA] |= wl.ACCEL_TAMPER_IMMEDIATE_DEFAULT
        self.OpSettings[wl.ACCEL_TAMPER_SIGMA] |= wl.ACCEL_TAMPER_HISTORICAL_DEFAULT << 8

        self.OpSettings[wl.ACCEL_TAMPER_SIGMA2] = 0
        self.OpSettings[wl.ACCEL_TAMPER_SIGMA2] |= wl.ACCEL_TAMPER_THRESHOLD_DEFAULT

        # #TINY_CAP settings
        self.OpSettings[wl.NRF_CAP_MULLION_TUNE] = 0
        self.OpSettings[wl.NRF_CAP_MULLION_TUNE] |= wl.NRF_CAP_THRESHOLD_DEFAULT
        self.OpSettings[wl.NRF_CAP_MULLION_TUNE] |= wl.NRF_CAP_OVERSAMPLES_DEFAULT << 8
        self.OpSettings[wl.NRF_CAP_MULLION_TUNE] |= wl.NRF_CAP_DGAIN_DEFAULT << 12
        self.OpSettings[wl.NRF_CAP_MULLION_TUNE] |= wl.NRF_CAP_AGAIN_DEFAULT << 14

        self.OpSettings[wl.NRF_CAP_SG_TUNE] = 0
        self.OpSettings[wl.NRF_CAP_SG_TUNE] |= wl.NRF_CAP_THRESHOLD_DEFAULT
        self.OpSettings[wl.NRF_CAP_SG_TUNE] |= wl.NRF_CAP_OVERSAMPLES_DEFAULT << 8
        self.OpSettings[wl.NRF_CAP_SG_TUNE] |= wl.NRF_CAP_DGAIN_DEFAULT << 12
        self.OpSettings[wl.NRF_CAP_SG_TUNE] |= wl.NRF_CAP_AGAIN_DEFAULT << 14
        self.OpSettings[wl.PROX_BITSTREAM_FORMAT] |= wl.PROX_ENABLE_48_BIT_MASK

        ### F2F specific

        # Accelermometer Sensitivity = F, 20 degree tilt
        self.OpSettings[wl.SENSITIVITY_INDEX] &= ~(wl.ACC_SENSITIVITY_MASK)
        self.OpSettings[wl.SENSITIVITY_INDEX] |= 0x0F00 ### ***ASK ABOUT THIS. IT JUST ADDS 0x0F00 back in after line 444 cleared it. Is it necessary?
        self.OpSettings[wl.EXT_OPERATION_INDEX] &= ~(wl.TAMPER_STABILITY_COUNT_MASK | wl.TAMPER_ACTIVE_COUNT_MASK)
        self.OpSettings[wl.EXT_OPERATION_INDEX] |= 0x5500  # 20 degree tilt tamper trigger

        # F2F D0/GRN LED Control Line is ADC controlled
        self.OpSettings[wl.ADC_BOUNDARY_INDEX] = wl.D0_GRN_LED_BOUNDARY

        # Enable Tamper Events
        self.OpSettings[wl.OPERATION_INDEX] |= wl.ENABLE_TAMPER_EVENTS

        # Clear the BLE_OVERRIDE_OSDP_AV_MASK
        self.OpSettings[wl.BLE_OPTIONS_1_INDEX] &= ~(wl.BLE_OVERRIDE_OSDP_AV_MASK)

        # BLE Connection AV Setup
        self.OpSettings[wl.BUILD_INDEX] |= wl.FW_BLE_AV_ACTION_MASK # Blinking LED

        # F2F has a unique HASH key value
        #self.KeyPadMap[11] = wl.KP_KEY_HASH_F2F

        # Amber LED is idle state. Blink Off on card reads
        self.OpSettings[wl.SENSITIVITY_INDEX] &= ~(0xFFFF)
        self.OpSettings[wl.LED_OPTIONS_1_INDEX] |= (wl.DEFAULT_LED_PWM_DUTY_CYCLES | wl.RED_GREEN_LEDS)

        # Set up the file transfer baud rate 57600, timeout 30 seconds
        self.OpSettings[wl.HOST_SP_OPTIONS_INDEX] &= ~(wl.HOST_SP_BAUD_RATE_MASK)
        self.OpSettings[wl.HOST_SP_OPTIONS_INDEX] |= wl.BR_57600
        self.OpSettings[wl.F2F_MCLP_INDEX] &= ~(wl.FT_TIMEOUT_MASK)
        self.OpSettings[wl.F2F_MCLP_INDEX] |= 0x1E00
        self.OpSettings[wl.F2F_MCLP_INDEX] |= 0x0004    # sets ASK to BCD format
        self.OpSettings[wl.F2F_MCLP_INDEX] |= 0x0010    # sets 40 bit Wiegand outputs to BCD

        # Set up as a non-uart interface
        self.OpSettings[wl.HOST_SP_OPTIONS_INDEX] &= (~wl.HOST_SP_PROTOCOL_MASK)

        # FSK, ASK (CASI_4002) is always supported
        self.OpSettings[wl.OPERATION_INDEX] |= (wl.ENABLE_ASK_RF | wl.ENABLE_FSK_RF)
        self.OpSettings[wl.WIEGAND_DATA_OPTIONS_INDEX] |= wl.WIEGAND_CASI_4002

        # Setup for a 2-State F2F reader (Note: Only Pepsico (CPE1) is 4-state F2F)
        self.OpSettings[wl.WIEGAND_DATA_OPTIONS_INDEX] &= ~(wl.F2F_OP_STATE_MASK)
        self.OpSettings[wl.WIEGAND_DATA_OPTIONS_INDEX] |= wl.F2F_2_STATE
        self.OpSettings[wl.WIEGAND_DATA_OPTIONS_INDEX] |= 8

    def setFilterMask(self, idx, mask):
        self.BsFilterMask[idx] = mask

    def setFilterValue(self, idx, value):
        self.BsFilterValue[idx] = value

    def setFilter(self, appliedFilter, bits, mask, value):
        if (len(mask) > wl.FILTER_MAX_BYTE_SIZE) or (len(value) > wl.FILTER_MAX_BYTE_SIZE):
            sys.exit("Error mask length or value to large")
        self.BsAppliedFilter = appliedFilter
        self.BsNumBits = bits
        self.BsFilterMask = mask[: wl.FILTER_MAX_BYTE_SIZE]
        self.BsFilterValue = value[: wl.FILTER_MAX_BYTE_SIZE]

    def setType(self, type):
        self.type = type

    def setKey(self, type, key):
        self.SecurityKeySets[type] = key

    def setGuardianKey(self, key):
        self.GuardianKey = key

    def setMobile(self, option, operation, value):
        if "MASK" == option:
            self.nfcConfig.mask(option, value)
        elif "AUG" == option:
            self.nfcConfig.aug(option, value)
        else:
            self.nfcConfig.set(option, value)           # this nfc confic gets appended to finalBin in dump

    def __init__(self):
        # self.name = name    # instance variable unique to each instance

        # # Note: All fields in this structure must remain in the same exact
        # #       relative location to maintain legacy compatibility.
        # #       New fields can be added only in the rfu_1[] and rfu_2[] areas.
        # typedef struct _SYSTEM_FEATURES_T
        # {
        #     # Operational Settings
        #     uint16_t OpSettings[MAX_OPTION_SETTINGS]   # 128
        # OpSettings = array.array('H')
        self.fAskHwSupport = False
        self.type = 0
        self.OpSettings = []
        # initialize option list
        for x in range(wl.MAX_OPTION_SETTINGS):
            self.OpSettings.append(0)
        # set default options
        self.__setDefaultOpSettings()
        #     # Mapped values for each key
        #     uint8_t KeyPadMap[MAX_KEY_PAD_BUTTONS]     # 16
        self.KeyPadMap = bytearray(wl.MAX_KEY_PAD_BUTTONS)
        for i in range(9):
            self.KeyPadMap[i] = i + 1
        self.KeyPadMap[9] = wl.KP_KEY_STAR
        self.KeyPadMap[11] = wl.KP_KEY_HASH_F2F
        # 	# BLE Mode and Advertised Name
        # 	uint8_t BleAdNameLen
        self.BleAdNameLen = 6
        # 	uint8_t BleAdName[MAX_BLE_AD_NAME_SIZE]    # 8
        self.BleAdName = "0Ethos"
        # 	# FW Version
        # 	uint8_t MainFwMajorVersion
        # 	uint8_t MainFwMinorVersion
        # 	uint8_t MainFwBuildNumber
        self.MainFwMajorVersion = wl.FW_MAJOR_VERSION
        self.MainFwMinorVersion = wl.FW_MINOR_VERSION
        self.MainFwBuildNumber = wl.FW_BUILD_NUMBER

        # 	# Wiegand Bit Stream Filter
        # 	uint8_t BsAppliedFilter
        # 	uint8_t BsNumBits
        # 	uint8_t BsFilterMask[FILTER_MAX_BYTE_SIZE]   # 8
        # 	uint8_t BsFilterValue[FILTER_MAX_BYTE_SIZE]  # 8
        self.BsAppliedFilter = 0
        self.BsNumBits = 0
        self.BsFilterMask = bytearray(wl.FILTER_MAX_BYTE_SIZE)
        self.BsFilterValue = bytearray(wl.FILTER_MAX_BYTE_SIZE)
        # self.BsFilterMask = ""
        # self.BsFilterValue = ""

        # 	uint8_t MainFwReleaseCandidate
        self.MainFwReleaseCandidate = wl.FW_RELEASE_CANDIDATE

        # 	# NFC configuration data
        # 	NFC_CONFIG_T nfcConfig    # 47
        self.nfcConfig = NFC_CONFIG()
        #     # Supported Rf Protocol Settings
        #     uint8_t RfProtocols[MAX_PROTOCOLS]    # 16
        self.RfProtocols = bytearray(wl.MAX_PROTOCOLS)
        #     # Supported Card Applications
        #     uint8_t CardTypesApps[MAX_CARD_TYPES][MAX_CARD_APPS]   # 184
        # self.CardTypesApps = [[0 for i in range(wl.MAX_CARD_TYPES)] for i in range(wl.MAX_CARD_APPS)]
        self.CardTypesApps = []
        for i in range(wl.MAX_CARD_TYPES):
            col = []
            for j in range(wl.MAX_CARD_APPS):
                col.append(wl.CA_NONE)
            self.CardTypesApps.append(col)

        for i in range(wl.MAX_VALID_CARD_TYPES):
            self.CardTypesApps[i][0] = wl.CA_CSN

        self.CardTypesApps[wl.CT_GENERIC_CL2][0] = wl.CA_NONE
        self.CardTypesApps[wl.CT_ECP_NFC][0] = wl.CA_NONE
        self.CardTypesApps[wl.CT_ISO_14443A_4][0] = wl.CA_NONE
        # 	# RFU - Not yet defined
        # 	uint8_t rfu_1[72]
        self.rfu_1 = bytearray(72)
        # 	uint8_t KgMap
        self.KgMap = 0x00
        # 	uint8_t BleSn[BLE_SN_SIZE]            # 8
        # self.BleSn = ""
        # 	uint8_t AtcaSn[AT_SN_SIZE]            # 9
        # self.AtcaSn = ""
        # 	uint8_t AtcaSecret[AT_SECRET_SIZE]    # 32
        # self.AtcaSecret = ""

        #     # Security Keys
        #     uint8_t SecurityKeySets[MAX_KEY_SETS][KEY_SET_SIZE]   # 512
        self.SecurityKeySets = []
        for i in range(wl.MAX_KEY_SETS):
            self.SecurityKeySets.append("")
        #     uint8_t GuardianKey[AES_128_KEY_SIZE]   # Kg1
        self.GuardianKey = ""
        #     uint16_t crc
        self.crc = 0
        # } SYSTEM_FEATURES_T
