import os
import unittest
from unittest.mock import patch, Mock 

from pathlib import Path
from unittest import TestCase
from configparser import MissingSectionHeaderError
import configparser

from apex_buildCfg import *

load_dotenv()

class TestApexConfigs(TestCase):


    def test_parse_to_ini_success(self):
        """
        Success test case for parse_to_dict
        """
        pathname = Path(__file__).parent.joinpath("test.ini")
        parsed_ini = parse_ini(pathname)

        self.assertTrue(isinstance(parsed_ini, configparser.ConfigParser))
        self.assertTrue(parsed_ini["keypad"]["idle_led_on"] == "false")
    
    def test_parse_to_ini_file_is_not_ini(self):
        """
        Test case for parse_to_dict where filename is not of tile type ini
        """
        pathname = Path(__file__).parent.joinpath("test.txt")

        with self.assertRaises(MissingSectionHeaderError):
            parse_ini(pathname)

    
    def test_populate_keysets_success(self):
        """
        Success test case for populate_keysets
        """
        keyset_ini = configparser.ConfigParser()
        keyset_ini.read_dict(
            {
                "keys": {
                    "slot00": "GENERIC:ZEROS_KEY",
                }
            }
        )
        keyset_ini = populate_keysets(keyset_ini)

        self.assertTrue(isinstance(keyset_ini, configparser.ConfigParser))
        self.assertTrue(keyset_ini["keys"]["slot00"] == "00000000000000000000000000000000")

    
    def test_populate_keysets_keys_section_does_not_exist(self):
        """
        Test case for populate_keysets where passed_dict does not contain a section called keys
        """
        keyset_ini = configparser.ConfigParser()
        keyset_ini.read_dict(
            {
                "test": {
                    "subTest": "testVal",
                }
            }
        )
        keyset_ini = populate_keysets(keyset_ini)

        self.assertIsNone(keyset_ini)
    
    
    def test_populate_keysets_keyset_id_improper_format(self):
        """
        Test case for populate_keysets where the value for a slot is not in format KEYSET:KEY
        """
        keyset_ini = configparser.ConfigParser()
        keyset_ini.read_dict(
            {
                "keys": {
                    "slot00": "ZEROS_KEY",
                }
            }
        )
        keyset_ini = populate_keysets(keyset_ini)

        self.assertIsNone(keyset_ini)
    
    
    def test_populate_keysets_request_failure(self):
        """
        Test case for populate_keysets where the request to Sequoia fails becasue the keyset does not exist
        """
        keyset_ini = configparser.ConfigParser()
        keyset_ini.read_dict(
            {
                "keys": {
                    "slot00": "Not_a_keyset:ZEROS_KEY",
                }
            }
        )

        with self.assertRaises(SystemExit) as method_call:
            populate_keysets(keyset_ini)
            self.assertEqual(method_call.exception.code, 1)

    
    def test_populate_custom_with_defaults_success(self):
        """
        Success test case for populate_custom_with_defaults
        """
        custom_ini = configparser.ConfigParser()
        custom_ini.read_dict(
            {
                'custom_test': {
                    'custom_test_key1':'custom_value1', 
                    'custom_test_key2':'custom_value2'
                }, 
                'default_test1': {
                    'default_key1':'val1',
                    'default_key2':'val2'
                },
            }
        )
        default_ini = configparser.ConfigParser()
        default_ini.read_dict(
            {
                'custom_test': {
                    'custom_test_key1':'custom_value1', 
                    'custom_test_key2':'custom_value2',
                },
                'default_test1': {
                    'default_key1':'val1',
                    'default_key2':'val2',
                    'default_key3':'val3',
                },
                'default_test2': {
                    'default_key1':'value1',
                },
            }
        )
        expected_out_ini = configparser.ConfigParser()
        expected_out_ini.read_dict(
            {
                'custom_test': {
                    'custom_test_key1':'custom_value1', 
                    'custom_test_key2':'custom_value2',
                },
                'default_test1': {
                    'default_key1':'val1',
                    'default_key2':'val2',
                    'default_key3':'val3',
                },
                'default_test2': {
                    'default_key1':'value1',
                },
            }
        )
        
        actual_out_ini = populate_custom_with_defaults(custom_ini, default_ini)
        self.assertEqual(actual_out_ini.sections(), expected_out_ini.sections())
        for section in expected_out_ini.sections():
            print(f'[{section}]')
            for name in expected_out_ini[section]:
                print(f'(expected) {name}: {expected_out_ini[section][name]}')
                print(f'(actual)   {name}: {actual_out_ini[section][name]}')
                self.assertTrue(name in actual_out_ini[section], f'"{name}" not found in "{actual_out_ini[section].name}"')
                self.assertEqual(actual_out_ini[section][name], expected_out_ini[section][name])

    def test_validate_custom_against_defaults_value_not_in_default(self):
        """
        Test case for validate_custom_against_defaults where the custom dictionary contains values not in the defualt dictionary
        """
        custom_ini = configparser.ConfigParser()
        custom_ini.read_dict(
            {
                'custom_test': {
                    'custom_test_key1':'custom_value1', 
                    'custom_test_key2':'custom_value2',
                }, 
                'default_test1': {
                    'default_key1':'val1',
                    'default_key2':'val2',
                },
                'doesnotexist': {
                    'test':'testVal',
                },
            }
        )
        default_ini = configparser.ConfigParser()
        default_ini.read_dict(
            {
                'default_test1': {
                    'default_key1':'val1',
                    'default_key2':'val2',
                    'default_key3':'val3',
                }, 
                'default_test2':{
                    'default_key1':'value1',
                },
                'custom_test': {
                    'custom_test_key1':'custom_value1', 
                    'custom_test_key2':'custom_value2',
                },
            }
        )
        
        with self.assertRaises(SystemExit) as method_call:
            validate_custom_against_defaults(custom_ini, default_ini)
            self.assertEqual(method_call.exception.code, 1)

    def test_write_to_temp_ini_success(self):
        """
        Success test case for write_to_temp_ini
        """
        passed_ini = configparser.ConfigParser()
        passed_ini.read_dict(
            {
                'custom_test':{
                    'custom_test_key1':'custom_value1', 
                    'custom_test_key2':'custom_value2',
                },
                'default_test1':{
                    'default_key1':'val1',
                    'default_key2':'val2',
                    'default_key3':'val3',
                },
                'default_test2':{
                    'default_key1':'value1',
                },
            }
        )
        filename = Path(__file__).parent.joinpath("testTemp.ini")

        with open(filename, 'w') as f:
            passed_ini.write(f)

        config = parse_ini(filename)

        self.assertTrue(config['custom_test']['custom_test_key2'] == "custom_value2")

        os.remove(filename)

    def test_encrypt_cbc_success(self):
        """
        Success test case for encrypt_cbc
        """
        plaintext = b'0abcdeadbeef00'
        ciphertext = encrypt_cbc(plaintext)

        self.assertNotEqual(plaintext, ciphertext)
        self.assertIsNotNone(ciphertext)

    
    def test_pad_success(self):
        """
        Success test case for pad
        """
        plaintext = b'deadbeef'
        padtext = pad(plaintext)

        self.assertTrue(len(padtext) % 16 == 0)

    def test_full_envelope_wrap_success(self):
        """
        Success test case for full_envelope_wrap
        """
        config_filename = Path('./config.ini')
        keyset_filename = Path('./keyset.ini')
        appcore_filename = Path('./appcore.bin')
        netcore_filename = Path('./netcore.bin')
        mcuboot_filename = Path('./mcuboot.bin')

        with open(config_filename, 'wb') as f:
            f.write(b'deadbeef')
        with open(keyset_filename, 'wb') as f:
            f.write(b'beefdead')
        with open(appcore_filename, 'wb') as f:
            f.write(b'deadbeef')
        with open(netcore_filename, 'wb') as f:
            f.write(b'deadbeef')
        with open(mcuboot_filename, 'wb') as f:
            f.write(b'deadbeef')

        wrapped = full_envelope_wrap(
            config_ini_path=config_filename, 
            keyset_ini_path=keyset_filename, 
            appcore_image_path=appcore_filename, 
            netcore_image_path=netcore_filename, 
            mcuboot_image_path=mcuboot_filename,
        )
        
        self.assertTrue(len(wrapped) == 92)

        os.remove(config_filename)
        os.remove(keyset_filename)
        os.remove(appcore_filename)
        os.remove(netcore_filename)
        os.remove(mcuboot_filename)
    
    def test_add_wrap_partial_success_no_keysets(self):
        """
        Success test case for add_wrap_partial with no keys section
        """
        config_filename = Path('./config.ini')
        with open(config_filename, 'wb') as f:
            f.write(b'deadbeef')

        wrapped = partial_envelope_wrap(config_ini_path=config_filename)
        
        self.assertTrue(len(wrapped) == 16)

    def test_add_wrap_partial_success_with_keysets(self):
        """
        Success test case for add_wrap_partial with a keys section
        """
        config_filename = Path('./config.ini')
        keyset_filename = Path('./keyset.ini')

        with open(config_filename, 'wb') as f:
            f.write(b'deadbeef')
        with open(keyset_filename, 'wb') as f:
            f.write(b'deadbeef')
            
        wrapped = partial_envelope_wrap(config_ini_path=config_filename, keyset_ini_path=keyset_filename)

        self.assertTrue(len(wrapped) == 26)


unittest.main()