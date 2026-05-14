MAX_KEY_SETS          = 16
KEY_SET_SIZE                  = 32
AES_128_KEY_SIZE      = 16

SecurityKeySets: list = []
for i in range(MAX_KEY_SETS):
    SecurityKeySets.append("")
#     uint8_t GuardianKey[AES_128_KEY_SIZE]   # Kg1
GuardianKey = ""
#     uint16_t crc
crc = 0

def genConfigKeys(keySet):
    finalBin = bytearray(0)
    for secKeySet in range(MAX_KEY_SETS):
        finalBin += SecurityKeySets[secKeySet].ljust(KEY_SET_SIZE, "\0").encode("ascii")
    finalBin += GuardianKey.ljust(AES_128_KEY_SIZE, "\0").encode("ascii")


def main():
    file = open('config/PROD_TEST_BUILD.bin', mode='rb')
    contents = file.read()
    file.close()

    contents += genConfigKeys("WaveLynx")
    print(contents)
if __name__ == "__main__":
    main()