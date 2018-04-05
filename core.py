# Version 1.0.0a1

import os
import time
import json
import config


class Others:
    def __init__(self):
        pass

    def scanForFiles(self, dir, delay=0.1):
        files = []

        for r, d, f in os.walk(dir):
            for file in f:
                if "" in file:
                    files.append(os.path.join(r, file))
                    time.sleep(config.core['scan-delay'])

        return files

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
        files_list = self.scanForFiles(options['path'])

        package['files'] = {}
        package['count'] = len(files_list)

        with open(save_file, 'w+') as file:
            json.dump(package, file)

    def getFilesContent(self, files):
        pass
