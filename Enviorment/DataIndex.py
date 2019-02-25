from NameData import NameData
import os

dataDir = r'C:\Users\Joshua\Desktop\PP5\Void-Web\Enviorment\data\nametypes'

class DataIndex():
    def __init__(self, dataPath):
        # __DATA_PATH__ is the folder in which pickled name files are stored
        self.__DATA_PATH__ = dataPath
        if not self.__DATA_PATH__.endswith('/'):
            self.__DATA_PATH__ += '/'

    def __loadNameData__(self, Name_Type):
        nameDataPath = self.__DATA_PATH__ + Name_Type
        return NameData(nameDataPath)

    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError(f"Provided key: '{key}' is not a valid Name_Type, or data for the Name_Type does not exist.")
        return self.__loadNameData__(key)

    def __len__(self):
        return len(os.listdir(self.__DATA_PATH__))

    def keys(self):
        return list(os.listdir(self.__DATA_PATH__))

    def items(self):
        for key in self.keys():
            yield (key, self.__getitem__(key))

    def values(self):
        for key in self.keys():
            yield self.__getitem__(key)

# DI = DataIndex(dataDir)

# print(DI.keys())
# input()
# for nameType in DI.keys():
#     print(DI[nameType].Tags)
# input()
# for value in DI.values():
#     print(value)
# input()
# print(DI['pokemon'].Tags)
# print(DI['pokemon'].Category)
# DI['pokemon'].Category = 'Places'
# print(DI['pokemon'].Category)
# input()
# DI['pokemon'].Category = 'Creatures'
# print(DI['pokemon'].Category)
# input()
