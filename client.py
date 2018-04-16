# Version 1.0.1a1
# https://github.com/Very1Fake/scp

import os
import sys
import scp
import config
import plugins.cap as cap
import plugins.af as af

sys.dont_write_bytecode = True


Core = scp.Core()
ConsoleParser = cap.cap(config.cap_config)

args, keys, long_keys = ConsoleParser.getArgs()
args = af.fillEmptyCell(args, 5)
use = False

# Additional commands by keys
if 'help' in long_keys:
    print('Help:')
    print(' \'create\' - create package with files in current dir')
    print(' \'extract\' - extract files from package in current dir')
    exit()
elif 'v' in keys:
    print(config.manager['ver'])
    exit()
elif 'version' in long_keys:
    print(config.manager['name'] + '\n' + config.manager['version'] + '\n' +
          config.manager['copyright'] + '\n\n' + cap.name + '\n' + cap.version)
    exit()

# Main commands by arguments
if args[0] == 'create' or args[0] == 'c':
    options = {}

    # Path of Source Code
    if 'path' in long_keys and long_keys['path'] != 'None':
        if os.path.exists(long_keys['path']):
            options['path'] = long_keys['path']
        else:
            af.exitEmergancy('Path doesn\'t exist')
    else:
        options['path'] = os.getcwd()

    # Name of Package
    if args[1] != '':
        options['name'] = args[1]
    else:
        if 'path' in long_keys:
            options['name'] = os.path.basename(long_keys['path'])
        else:
            options['name'] = os.path.basename(os.getcwd())

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

    if Core.packPackage(options) is True:
        print('Package create success')
    exit()

if args[0] == 'extract' or args[0] == 'x':
    options = {}

    # Path of Package
    if 'path' in long_keys:
        if os.path.exists(long_keys['path']):
            options['path'] = long_keys['path']
        else:
            af.exitEmergancy('Path doesn\'t exist')
    else:
        options['path'] = os.getcwd()

    # Name of Package
    if args[1] == '':
        af.exitEmergancy('The package name is not specified')
    else:
        if os.path.exists(options['path'] + '/' + args[1]):
            options['name'] = args[1]
        else:
            af.exitEmergancy('Package doesn\'t exist')

    # Path to extract
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

    if Core.unpackPackage(options) is True:
        print('Package extract success')
    exit()
elif args[0] == 'list' or args[0] == 'l':
    options = {}

    # Path of Package
    if 'path' in long_keys:
        if os.path.exists(long_keys['path']):
            options['path'] = long_keys['path']
        else:
            af.exitEmergancy('Path doesn\'t exist')
    else:
        options['path'] = os.getcwd()

    # Name of Package
    if args[1] == '':
        af.exitEmergancy('The package name is not specified')
    else:
        if os.path.exists(options['path'] + '/' + args[1]):
            options['name'] = args[1]
        else:
            af.exitEmergancy('Package doesn\'t exist')

    # Path to extract
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

    files = Core.listFilesInPackage(options)

    print('Files in ' + options['name'] + ':')
    for i in files:
        print(' ' + i)

    exit()

print('Try \'scpm --help\' to see all commands')
