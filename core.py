# Version 1.0.0a1

import os
import time
import json
import config
import hashlib


class Others:
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


class Core(Others):
    def __init__(self):
        pass

    def packPackage(self, options):
        package = {}
        package['name'] = options['name']
        package['version'] = config.core['v']

        save_file = package['name'] + '.scp'
        file_list = self.scanForFiles(options['path'])

        package['files'] = self.getFileList(file_list, options['path'])
        package['count'] = len(file_list)

        with open(save_file, 'w+') as file:
            json.dump(package, file)

    def unpackPackage(self, options):
        package = {}

    def getFileList(self, files, cutpath, i=1):
        file_list = {}

        for f in files:
            file_list['f' + str(i)] = {
                'name': f.split('/')[-1],
                'path': self.getCutFullPath(f, cutpath),
                'content': self.getFileContent(f)
            }

            if config.core['debug'] == 1:
                print(file_list['f' + str(i)])

            i += 1
            time.sleep(config.core['delay'])

        return file_list

    def getFileContent(self, file):
        content = open(file, 'r').readlines()
        return ''.join(content)
