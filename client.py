# Version 1.0.0a1

import core
import plugins.cap
import config
import os


Others = core.Others()
TerminalParser = plugins.cap.cap(config.cap_config)

args, keys, long_keys = TerminalParser.getArgs()
args = Others.fillEmptyCell(args, 5)
print(args)

if 'help' in long_keys:
    print('Help:')
elif 'v' in keys:
    print(config.ver)
elif 'version' in long_keys:
    print(config.name + '\n' + config.version + '\n\n' + plugins.cap.name + '\n' + plugins.cap.version)
elif args[0] == 'n':
    options = {}

    # Name of Package
    if 'name' in long_keys:
        options['name'] = long_keys['name']
    else:
        if 'path' in long_keys:
            options['name'] = os.path.basename(long_keys['path'])
        else:
            options['name'] = os.path.basename(os.getcwd())

    # Path of Source Code
    if 'path' in long_keys:
        options['path'] = long_keys['path']
    else:
        options['path'] = os.getcwd()

    # Path of Package
    if 'save' in long_keys:
        if long_keys['save'] == 'None':
            options['save'] = os.getcwd()
        else:
            options['save'] = long_keys['save']
    elif 'saveto' in long_keys:
        if long_keys['saveto'] == 'None':
            options['save'] = os.getcwd()
        else:
            options['save'] = long_keys['saveto']
    else:
        options['save'] = options['path']


    print(options)
else:
    print('Try \'scpm --help\' to see all commands')
