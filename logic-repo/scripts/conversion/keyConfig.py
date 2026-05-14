# keyConfig.py
# argv1 must be the eKey from the firmware if this is being used for key extraction

import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import sys
import binascii
keyId = "keyID_"

#buffer =  open("../../../WallMountReader/WallMountReader/src/UserKeys.c").read()
buffer =  open("../../../WallMountReader/src/UserKeys.c").read()

final = buffer
keyName= 0
keyIterator =0
buffer = buffer.replace('{\n','')
writer = open("ETHOS.keyfile", "wt")

match = re.findall(r'{.*?}|#ifdef',buffer, re.DOTALL  )
backend = default_backend()
def _decrypt_ecb(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def _encrypt_ecb(plaintext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

keyIterator = 0

# print(match)
for key in match:
    replaceKey = key

    #make sure to reset the internal obfuscation counter on an ifdef
    if ( -1 != key.find("#ifdef")):
        keyIterator = 0
        continue
    if (bool (re.search(key, buffer, re.DOTALL))==True):
        keyName = keyName +1
        key =key.replace('{','')
        key = key.replace('}','')
        key = key.replace(',','')
        key = key.replace('0x','')
        key = key.replace('\t','')
        key = key.replace(' ','')
        key = key.strip()
        key = re.sub('\s*\/\/.*','', key)
        # key = re.sub(',\s*\n\s*','', key)
        key = key.replace('\n','')
        key = key.strip()
        eKey = bytearray.fromhex(sys.argv[1])
       # print ("START eKey", binascii.hexlify(eKey))
        eKey[0] = keyIterator
       # print("eKey", binascii.hexlify(eKey))

        print ("\n\noriginal", key)
        decKey = _decrypt_ecb(bytes.fromhex(key),eKey)
        print ("decoded", binascii.hexlify(decKey))
        newkey= bytearray(16)
        #print (newkey)
        newkey[0] = keyIterator << 1
        print ("GUARDKEY ",newkey)
        print(len(decKey))
        print ("output ",(_encrypt_ecb(decKey[0:16],newkey)).hex())
        newkey[0] = (  keyIterator << 1) + 1
        print ("GUARDKEY odd ",newkey)
        print ("output odd ",(_encrypt_ecb(decKey[16:32],newkey)).hex())

        writer.write(keyId+str(keyName) +"_a:"+ (decKey.hex()[0:32]) + "\n")
        writer.write(keyId+str(keyName) +"_b:"+ (decKey.hex()[32:64]) + "\n")
    buffer = buffer.replace(replaceKey,keyId+str(keyName) )
    #keys are obfuscated by taking the location and shifting in to the gKey so this needs to be tracked seperately from the keyName
    keyIterator = (keyIterator +1)%16


buffer = re.sub('\(.*\)','', buffer)
# buffer = re.sub('#.*','\n', buffer)
writer.close()

# dont find me to ask why I did it this way but it seems to work.....
#replace newline with a comma
buffer = buffer.replace('\n',',')
# now remove the  resulting ,, from the above command and replace it with a newline
buffer = buffer.replace(',,','')
buffer = buffer.replace('{','')
buffer = buffer.replace('}','')
buffer = buffer.replace('//','\n')
buffer = buffer.replace('#endif','\n')
# buffer = re.sub('\s*,\s*',',', buffer)
buffer = buffer.replace(',,','\n')
buffer = buffer.replace('/,','/\n')
buffer = buffer.replace('#if','\n\n#if')

print(buffer.strip())

