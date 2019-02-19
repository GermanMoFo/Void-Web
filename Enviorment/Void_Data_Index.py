

# class DataIndex:
#     def __init__(self, dataPath):
#         self.__dataPath__ = dataPath
        

#     def __createIndex__(self, dataPath):
#         #helper function, yields all files in a directory
#         def files(path):  
#             for file in os.listdir(path):
#                 if os.path.isfile(os.path.join(path, file)):
#                     yield file

#         index = {}
#         for file in files(path):
#             key = file.split('.')[0]
#             index[key] = path + file
#         return index

class Name_Data:
    def __init__(self, directory):
        self.__dataDirectory__ = directory
        if not self.__dataDirectory__.endswith("/"):
            self.__dataDirectory__ += '/'

    def __loadJSON__(self, file):
        # Simple helper function that loads the given json file from __dataDirectory__
        from json import load

        with open(self.__dataDirectory__ + file, 'r') as f:
            return load(f)

    def __saveJSON__(self, file, data):
        from json import dump
        with open(self.__dataDirectory__ + file, 'w') as f:
            dump(data, f, indent=4, sort_keys=True)

    def __loadMetaData__(self):
        return self.__loadJSON__('meta.json')

    def __loadRawData__(self):
        return self.__loadJSON__('raw.json')

    def __loadDictionary__(self):
        return self.__loadJSON__('dictionary.json')

    def __saveMetaData__(self, data):
        return self.__saveJSON__('meta.json', data)

    def __saveRawData__(self, data):
        return self.__saveJSON__('raw.json', data)

    def __saveDictionary__(self, data):
        return self.__saveJSON__('dictionary.json', data)

    @property
    def Tags(self):
        return self.__loadMetaData__()['Tags']

    @Tags.setter
    def Tags(self, value):
        from copy import copy

        currentMetaData = self.__loadMetaData__()
        newMetaData = copy(currentMetaData)
        newMetaData['Tags'] = value
        self.__saveMetaData__(newMetaData)

    @property
    def Category(self):
        return self.__loadMetaData__()['Category']

    @Category.setter
    def Category(self, value):
        from copy import copy

        currentMetaData = self.__loadMetaData__()
        newMetaData = copy(currentMetaData)
        newMetaData['Category'] = value
        self.__saveMetaData__(newMetaData)

    @property
    def Proper(self):
        return self.__loadMetaData__()['Proper']

    @Proper.setter
    def Proper(self, value):
        from copy import copy

        currentMetaData = self.__loadMetaData__()
        newMetaData = copy(currentMetaData)
        newMetaData['Proper'] = value
        self.__saveMetaData__(newMetaData)

    @property
    def RawData(self):
        return self.__loadRawData__()['Data']

    @RawData.setter
    def RawData(self, value):
        from copy import copy

        currentRawData = self.__loadRawData__()
        newRawData = copy(currentRawData)
        newRawData['Data'] = value
        self.__saveRawData__(newRawData)

    @property
    def MarkovDictionary(self):
        return self.__loadDictionary__()

    @MarkovDictionary.setter
    def MarkovDictionary(self, value):
        from copy import copy

        currentDictionary = self.__loadDictionary__()
        newDictionary = copy(currentDictionary)
        newDictionary = value
        self.__saveDictionary__(newDictionary)
    
nd = Name_Data(r'C:\Users\Joshua\Desktop\PP5\Void-Web\Enviorment\data\nametypes\americanCities')
print(nd.RawData)
print(nd.Tags)
print(nd.Category)
print(nd.Proper)
nd.Category = 'Creatures'
print(nd.Category)
nd.Category = 'Places'
    