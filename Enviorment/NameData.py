class NameData:

    class TagView():
        def __init__(self, nameData):
            self.__metaFilePath__ = nameData.__dataDirectory__ + 'meta.json'
            self.__nameData__ = nameData

        def __loadTags__(self):
            metaData = self.__nameData__.__loadMetaData__()
            return metaData['Tags']
        def __saveTags__(self, tags):
            from copy import copy
            currentMetaData = self.__nameData__.__loadMetaData__()
            newMetaData = copy(currentMetaData)
            newMetaData['Tags'] = tags
            self.__nameData__.__saveMetaData__(newMetaData)
        def __str__(self):
            return str(self.__loadTags__())
        def __len__(self):
            return self.__loadTags__().__len__()
        def __iter__(self):
            return self.__loadTags__().__iter__()
        def __getitem__(self, index):
            return self.__loadTags__().__getitem__(index)
        def __contains__(self, item):
            return self.__loadTags__().__contains__(item)
        def append(self, tag):
            newTagList = self.__loadTags__()
            newTagList.append(tag)
            self.__saveTags__(newTagList)
        def remove(self, value):
            newTagList = self.__loadTags__()
            result = newTagList.remove(value)
            self.__saveTags__(newTagList)
            return result
        def clear(self):
            self.__saveTags__([])

    class DataView():
        def __init__(self, nameData):
            self.__nameData__ = nameData

        def __loadData__(self):
            rawData = self.__nameData__.__loadRawData__()
            return rawData['Data']
        def __saveData__(self, data):
            from copy import copy
            currentRawData = self.__nameData__.__loadRawData__()
            newRawData = copy(currentRawData)
            newRawData['Data'] = data
            self.__nameData__.__saveRawData__(newRawData)
        def __str__(self):
            return str(self.__loadData__())
        def __len__(self):
            return self.__loadData__().__len__()
        def __iter__(self):
            return self.__loadData__().__iter__()
        def __getitem__(self, index):
            return self.__loadData__().__getitem__(index)
        def __contains__(self, item):
            return self.__loadData__().__contains__(item)
        def append(self, data):
            newDataList = self.__loadData__()
            newDataList.append(data)
            self.__saveData__(newDataList)
        def remove(self, value):
            newDataList = self.__loadData__()
            result = newDataList.remove(value)
            self.__saveData__(newDataList)
            return result
        def clear(self):
            self.__saveData__([])

    class DictionaryView():
        def __init__(self, nameData):
            self.__nameData__ = nameData
        def __loadDict__(self):
            markovDict = self.__nameData__.__loadDictionary__()
            return markovDict
        def __saveDict__(self, data):
            from copy import copy
            self.__nameData__.__saveDictionary__(data)
        def __str__(self):
            return str(self.__loadDict__())
        def __len__(self):
            return self.__loadDict__().__len__()
        def __iter__(self):
            return self.__loadDict__().__iter__()
        def __getitem__(self, key):
            return self.__loadDict__().__getitem__(key)
        def __setitem__(self, key, value):
            markovDict = self.__loadDict__()
            markovDict[key] = value
            self.__saveDict__(markovDict)
        def __contains__(self, item):
            return self.__loadDict__().__contains__(item)
        def values(self):
            return self.__loadDict__().values()
        def keys(self):
            return self.__loadDict__().keys()
        def pop(self, key):
            newDictionary = self.__loadDict__()
            result = newDictionary.pop(key)
            self.__saveDict__(newDictionary)
            return result
        def clear(self):
            self.__saveDict__({})

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
        return self.TagView(self)
        
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
        return self.DataView(self)

    @RawData.setter
    def RawData(self, value):
        from copy import copy

        currentRawData = self.__loadRawData__()
        newRawData = copy(currentRawData)
        newRawData['Data'] = value
        self.__saveRawData__(newRawData)

    @property
    def MarkovDictionary(self):
        return self.DictionaryView(self)

    @MarkovDictionary.setter
    def MarkovDictionary(self, value):
        from copy import copy

        currentDictionary = self.__loadDictionary__()
        newDictionary = copy(currentDictionary)
        newDictionary = value
        self.__saveDictionary__(newDictionary)
    

# nd = NameData(r'C:\Users\thepe_000\Desktop\PP5\Void-Web\Enviorment\data\nametypes\americanCities')
# print(nd.RawData)
# for data in nd.RawData:
#     print(data)

# nd.RawData.append('Apple')
# print(nd.RawData)
# nd.RawData.remove('Apple')
# print(nd.RawData)

# temp = []
# for dat in nd.RawData:
#     temp.append(dat)

# nd.RawData.clear()
# print(nd.RawData)
# nd.RawData = temp
# print(nd.RawData)
# print(nd.MarkovDictionary)
# input()
# for key in nd.MarkovDictionary.keys():
#     print(key)
# input()
# for value in nd.MarkovDictionary.values():
#     print(value)
# input()

# nd.MarkovDictionary['apple'] = 'General Kenobi'
# print(nd.MarkovDictionary['apple'])
# print(nd.MarkovDictionary.pop('apple'))
# input()

# from copy import copy
# temp = copy(nd.MarkovDictionary.__loadDict__())
# nd.MarkovDictionary.clear()
# print(nd.MarkovDictionary)
# input()
# nd.MarkovDictionary = temp
# print(nd.MarkovDictionary)