# Version 1.0.0r Stable
# https://github.com/Very1Fake/scp

import sys

sys.dont_write_bytecode = True


# CAP config
cap_config = {
    'long-keys': 'allow',
    'long-keys-values': 'allow',
    'none-value': 'None',
    'delay': 0,
    'keys-limit': -1
}

# Main information (Manager)
manager = {
    'name': 'Source Code Package Manager',
    'version': 'Version 1.0.0r Stable',
    'ver': 'v1.0.0r Stable',
    'copyright': '(c) 2017 LightPixel GNU AGPL v3'
}

# Main information (Core)
scp = {
    'version': 101,
    'delay': 0.01,
    'debug': 0
}
