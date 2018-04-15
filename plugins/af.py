import sys

sys.dont_write_bytecode = True


# Additional functions
def exitEmergancy(msg=''):
    print('Emergancy exit')

    if msg != '':
        print('Reason: ' + msg)

    exit()


def fillEmptyCell(array, count=5):
    for i in range(count):
        array.append('')

    return array
