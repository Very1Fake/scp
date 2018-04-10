# Version 1.0.0a3
# https://github.com/Very1Fake/scp

import sys
import time

sys.dont_write_bytecode = True
name = 'Console Arguments Parser'
version = 'Version 1.0.0a3'


class cap:
    # Errors
    def BadConfig(Exception):
        pass

    def checkConfig(self, config):
        try:
            if not config['long-keys']:
                pass
        except KeyError:
            config['long-keys'] = 'allow'
        try:
            if not config['long-keys-values']:
                pass
        except KeyError:
            config['long-keys-values'] = 'allow'
        try:
            if not config['none-value']:
                pass
        except KeyError:
            config['none-value'] = 'None'
        try:
            if not config['delay']:
                pass
        except KeyError:
            config['delay'] = 0
        try:
            if not config['keys-limit']:
                pass
        except KeyError:
            config['keys-limit'] = -1

        return config

    def __init__(self, config=None):
        if config is None:
            self.BadConfig()
        else:
            self.config = config

    def getArgs(self, string=None):
        time.sleep(self.config['delay'])

        if self.config['long-keys-values'] == 'allow':
            long_keys = {}
        else:
            long_keys = []
        keys = []
        keys_left = self.config['keys-limit']
        args = []
        z = 0

        if string is None:
            string = sys.argv

        while True:
            z += 1
            try:
                if string[z][:2] == '--' and self.config['long-keys'] != 'deny':
                    if self.config['long-keys-values'] == 'allow':
                        try:
                            long_keys[string[z][2:]] = string[z+1]
                        except IndexError:
                            long_keys[string[z][2:]] = self.config['none-value']
                        z += 1
                    else:
                        long_keys.append(string[z][2:])
                elif string[z][:1] == '-':
                    temp = list(string[z][1:])
                    for n in temp:
                        if keys_left > 0 or keys_left < 0:
                            keys_left -= 1
                            keys.append(n)
                else:
                    args.append(string[z])
            except IndexError:
                break

        if self.config['long-keys'] != 'deny':
            return args, keys, long_keys
        else:
            return args, keys
