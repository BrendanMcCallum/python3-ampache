#!/usr/bin/env python3

import sys

import ampache

# user variables
ampache_url = 'https://music.server'
ampache_api = 'mysuperapikey'
ampache_user = 'myusername'

# xml or json supported formats
api_format = 'json'

"""
encrypt_string
"""
encrypted_key = ampache.encrypt_string(ampache_api, ampache_user)

"""
handshake
"""
print('Connecting to:\n    ', ampache_url)
src_api = ampache_api
ampache_api = ampache.handshake(ampache_url, encrypted_key, False, False, '400004', api_format)

print('\nThe ampache handshake for:\n    ', src_api, '\n\nReturned the following session key:\n    ', ampache_api)
if not ampache_api:
    print()
    sys.exit('ERROR: Failed to connect to ' + ampache_url)
