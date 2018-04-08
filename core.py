# Version 1.0.0a1

import os
import time
import json
import config
import base64
import codecs


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

        with codecs.open(save_file, 'w+', errors='ignore') as f:
            f.write(bytes(json.dumps(package)))
            f.close()

    def unpackPackage(self, options):
        package = {}
        # f.split('/')[-1]
        with codecs.open(options['path']):
            pass

    def getFileList(self, files, cutpath, i=1):
        file_list = {}

        for f in files:
            file_list['f' + str(i)] = {
                'name': self.getCutFullPath(f, cutpath),
                'content': self.getFileContent(f)
            }

            if config.core['debug'] == 1:
                print(file_list['f' + str(i)])

            i += 1
            time.sleep(config.core['delay'])

        return file_list

    def getFileContent(self, file):
        with codecs.open(file, 'rb', errors='ignore') as f:
            content = base64.b64encode(f.read())
            content = content.decode('utf-8')
            f.close()
        return content
