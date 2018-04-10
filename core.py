# Version 1.0.0rc1
# https://github.com/Very1Fake/scp

import os
import sys
import time
import json
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
                    time.sleep(config.core['delay'])

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

    def packPackage(self, options):
        package = {}
        package['name'] = options['name']
        package['version'] = config.core['v']

        file = options['save'] + '/' + package['name'] + '.scp'
        file_list = self.scanForFiles(options['path'])

        package['files'] = self.getFileList(file_list, options['path'])
        package['count'] = len(file_list)

        with codecs.open(file, 'wb+', errors='ignore') as f:
            f.write(bytes(json.dumps(package)))
            f.close()

    def unpackPackage(self, options):
        file = options['path'] + '/' + options['name']

        package = self.getPackage(file)

        for i in package['files']:
            n, d = self.getFileInfo(i['name'], options['save'])
            c = i['content']
            self.checkDirectory(d)
            self.createFileWithContent(d + n, c)

    def getFileList(self, files, cutpath, i=0):
        file_list = []

        for f in files:
            file_list.append({
                'name': self.getCutFullPath(f, cutpath),
                'content': self.getFileContent(f)
            })

            if config.core['debug'] == 1:
                print(file_list[i])

            i += 1
            time.sleep(config.core['delay'])

        return file_list

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
        n = '/' + info.split('/')[-1:][0].encode('ascii')
        d = position + '/'.join(info.split('/')[:-1]).encode('ascii')
        return n, d

    def createFileWithContent(self, file, content):
        with open(file, 'wb+') as f:
            f.write(bytes(content.decode('base-64')))
            f.close()
