# Ethos Config

# Apex Config
The scripts contained in the apex folder of this repo take in custom configuration settings as a .ini file and convert them to an encrypted binary file
## Usage
`python3 apex_buildCfg.py -f file.ini`
## .ini file format
.ini files are broken into sections with keys and values underneath them. For example, if I have a section called section 1, that needs to store the values for key1, key2, and key3, it will be formated as
```
[section1]
key1 = value1
key2 = value2
key3 = value3
```
## .env file
.env file should contain:
    SEQUOIA_IP=[IP address for Sequoia]
    SEQUOIA_PORT=[port for Sequoia]
    BASE_URL=https://${SEQUOIA_IP}:${SEQUOIA_PORT}/
    TOKEN=[token for Sequoia usage]
    ENCRYPT_KEYSET=[name of the keyset in Sequoia that contains the key that will encrypt the config]
    ENCRYPT_KEY=[name of the key in Sequoia that will encrypt the config]