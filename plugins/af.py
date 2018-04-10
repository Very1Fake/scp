import sys

sys.dont_write_bytecode = True


# Additional functions
def exitEmergancy(msg=''):
    print('Emergancy exit')

    if msg != '':
        print('Reason: ' + msg)

    exit()
