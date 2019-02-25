from void_scribe.NameDataSource import NameDataSource

class LocalVoidWebDataSource(NameDataSource):
    
    def __init__(self, dataFilesPath):
        import DataIndex
        self.dataFilesPath = dataFilesPath
        self.dataIndex = DataIndex.DataIndex(self.dataFilesPath)

    def MarkovDictionary(self, nameTypes):
        data = {}
        for nameType in nameTypes:
            if nameType not in self.dataIndex.keys():
                raise ValueError(f'{nameType} is not a supported Name Type.')
            data[nameType] = {}
            data[nameType]['dictionary'] = self.dataIndex[nameType].__loadDictionary__()
        return data

    def RawData(self, nameTypes):
        data = {}
        for nameType in nameTypes:
            if nameType not in self.dataIndex.keys():
                raise ValueError(f'{nameType} is not a supported Name Type.')
            data[nameType] = {}
            data[nameType]['raw'] = self.dataIndex[nameType].__loadRawData__()
        return data

    def MetaData(self, nameTypes):
        data = {}
        for nameType in nameTypes:
            if nameType not in self.dataIndex.keys():
                raise ValueError(f'{nameType} is not a supported Name Type.')
            data[nameType] = {}
            data[nameType]['meta'] = self.dataIndex[nameType].__loadMetaData__()
        return data

    def Data(self, nameTypes):
        data = {}
        for nameType in nameTypes:
            if nameType not in self.dataIndex.keys():
                raise ValueError(f'{nameType} is not a supported Name Type.')
            data[nameType] = {}
            data[nameType]['meta'] = self.dataIndex[nameType].__loadMetaData__()
            data[nameType]['dictionary'] = self.dataIndex[nameType].__loadDictionary__()
            data[nameType]['raw'] = self.dataIndex[nameType].__loadRawData__()
        return data

    def Tags(self, nameTypes):
        metaData = self.MetaData(nameTypes)
        tagData = {}
        for nameType in metaData.keys():
            tagData[nameType] = {}
            tagData[nameType]['Tags'] = metaData[nameType]['meta']['Tags']
        return tagData


    def Category(self, nameTypes):
        metaData = self.MetaData(nameTypes)
        catData = {}
        for nameType in metaData.keys():
            catData[nameType] = {}
            catData[nameType]['Category'] = metaData[nameType]['meta']['Category']
        return catData

    def Proper(self, nameTypes):
        metaData = self.MetaData(nameTypes)
        propData = {}
        for nameType in metaData.keys():
            propData[nameType] = {}
            propData[nameType]['Proper'] = metaData[nameType]['meta']['Proper']
        return propData

    def GenerationData(self, nameTypes):
        metaData = self.MetaData(nameTypes)
        data = {}
        for nameType in metaData.keys():
            if nameType not in self.dataIndex.keys():
                raise ValueError(f'{nameType} is not a supported Name Type.')
            data[nameType] = {}
            data[nameType]['meta'] = self.dataIndex[nameType].__loadMetaData__()
            data[nameType]['dictionary'] = self.dataIndex[nameType].__loadDictionary__()
        return data

    def NameTypes(self):
        nameTypes = self.dataIndex.keys()
        return list(nameTypes)