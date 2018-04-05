# Version 1.0.0a1

import os


class Core:
    def __init__(self):
        pass




class Others:
    def __init__(self):
        pass

    def scanForFolders(self, dir):
        files = []

        for r, d, f in os.walk(dir):
            for file in f:
                if "" in file:
                    files.append(os.path.join(r, file))
                    time.sleep()

        return files

    def fillEmptyCell(self, array, count=5):
        for i in range(count):
            array.append('')

        return array
