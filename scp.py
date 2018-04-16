# Version 1.0.1a1
# https://github.com/Very1Fake/scp

import os
import sys
from time import sleep
from json import dumps, loads
import config
import base64

sys.dont_write_bytecode = True


class Core():
    def __init__(self):
        pass

    def getPackageFirstLine(self, name, count, version=config.scp['version']):
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
                                               config.scp['version']))

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
                f.close()

        package.close()
        return True

    def unpackPackage(self, options):
        # Package information
        file = options['path'] + '/' + options['name']
        package = open(file, 'r')
        info = loads(package.readline().encode('utf-8'))

        for i in range(info['count']):
            file = loads(package.readline()[:-1])
            n, d = self.getFileInfo(file[0], options['save'])
            self.checkDirectory(d)
            self.createFileWithContent(d + n, package.readline())

        package.close()
        return True

    def listFilesInPackage(self, options):
        file = options['path'] + '/' + options['name']
        package = open(file, 'r')
        info = loads(package.readline().encode('utf-8'))
        files = []

        for i in range(info['count']):
            files.append(loads(package.readline()[:-1])[0].encode('utf-8'))
            package.readline()

        return files

    def scanForFiles(self, dir, delay=0.1):
        files = []

        for r, d, f in os.walk(dir):
            for file in f:
                if "" in file:
                    temp = os.path.join(r, file)
                    files.append(temp)
                    sleep(config.scp['delay'])

        return files

    def getCutFullPath(self, path, cut):
        path = path[len(cut):]
        return path

    def checkDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def getFileInfo(self, info, position):
        n = '/' + info.split('/')[-1:][0].encode('utf-8')
        d = position + '/'.join(info.split('/')[:-1]).encode('utf-8')
        return n, d

    def createFileWithContent(self, file, content):
        with open(file, 'wb+') as f:
            f.write(bytes(content.decode('base-64')))
            f.close()
