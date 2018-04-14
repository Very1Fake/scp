# Version 1.0.0rc2
# https://github.com/Very1Fake/scp

import os
import sys
from time import sleep
from json import dumps, loads
import config
import base64
import codecs

sys.dont_write_bytecode = True


class Others():
    def __init__(self):
        pass

    def scanForFiles(self, dir, delay=0.1):
        files = []

        for r, d, f in os.walk(dir):
            for file in f:
                if "" in file:
                    temp = os.path.join(r, file)
                    files.append(temp)
                    if config.core['debug'] == 1:
                        print(temp)
                    sleep(config.core['delay'])

        return files

    def getCutFullPath(self, path, cut):
        path = path[len(cut):]
        return path

    def fillEmptyCell(self, array, count=5):
        for i in range(count):
            array.append('')

        return array

    def checkDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)


class Core(Others):
    def __init__(self):
        pass

    def getPackageFirstLine(self, name, count, version=config.core['version']):
        line = {}
        line['name'] = name
        line['version'] = version
        line['count'] = count
        return line

    def getPackageFileInfo(self, name, cut, position):
        info = [name[len(cut):], position]
        return info

    def packPackage(self, options):
        file_list = self.scanForFiles(options['path'])

        # Get first two lines
        line1 = dumps(self.getPackageFirstLine(options['name'],
                                               len(file_list),
                                               config.core['version']))

        # Init File
        file = options['save'] + '/' + options['name'] + '.scp'
        package = open(file, 'w+')
        package.write(line1)

        # Write Files Content
        z = 0
        for i in file_list:
            z += 1
            with open(i, 'rb') as f:
                package.write('\n' + dumps(
                    self.getPackageFileInfo(i, options['path'], z)))
                package.write('\n' + base64.b64encode(
                    f.read()))

        package.close()

    def unpackPackage(self, options):
        file = options['path'] + '/' + options['name']

        package = open(file, 'r')

        info = loads(package.readline().encode('utf-8'))

        for i in range(info['count']):
            file = loads(package.readline()[:-1])
            n, d = self.getFileInfo(file[0], options['save'])
            self.checkDirectory(d)
            with open(d + n, 'wb+') as f:
                f.write(bytes(package.readline().decode('base-64')))
                f.close()
            print(file, n, d, i)

        package.close()

    def getFileContent(self, file):
        with codecs.open(file, 'rb', errors='ignore') as f:
            content = base64.b64encode(f.read())
            content = content.decode('utf-8')
            f.close()
        return content

    def getPackage(self, file):
        with codecs.open(file, 'rb') as f:
            temp = json.loads(f.read().encode('ascii', 'ignore'))
            f.close()
            return temp

    def getFileInfo(self, info, position):
        n = '/' + info.split('/')[-1:][0].encode('utf-8')
        d = position + '/'.join(info.split('/')[:-1]).encode('utf-8')
        return n, d

    def createFileWithContent(self, file, content):
        with open(file, 'wb+') as f:
            f.write(bytes(content.decode('base-64')))
            f.close()
