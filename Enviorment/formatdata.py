# import os
# import json
# import pickle

# new_data_path = 'C:/Users/thepe_000/Desktop/PP5/Void-Web/Enviorment/Active/data/nametypes/'
# namesdata_path = 'C:/Users/thepe_000/Desktop/PP5/Void-Scribe/void_scribe/data/Names/'
# dictionaries_path = 'C:/Users/thepe_000/Desktop/PP5/Void-Scribe/void_scribe/data/MarkovDictionaries/'

# name_data_files = os.listdir(namesdata_path)
# dictionary_files = os.listdir(dictionaries_path)
# file_count = len(name_data_files)

# for index in range(0, file_count):
#     name_data = pickle.load(open(namesdata_path + name_data_files[index], "rb"))
#     dictionary_data = pickle.load(open(dictionaries_path + dictionary_files[index], "rb"))

#     meta_data = {}
#     raw_data = {}
    
#     meta_data['Tags'] = name_data['Tags']
#     meta_data['Category'] = name_data['Category']
#     meta_data['Proper'] = False

#     raw_data['Data'] = name_data['Data']

#     string_dictionary_data = {}
#     for key in dictionary_data.keys():
#         new_key = "".join(key)
#         string_dictionary_data[new_key] = dictionary_data[key]

#     name_data_subdirectory = new_data_path + name_data_files[index].split('.')[0] + '/'
#     os.mkdir(name_data_subdirectory)

#     with open(name_data_subdirectory + 'meta.json', 'w') as f:
#         json.dump(meta_data, f, indent=4, sort_keys=True)

#     with open(name_data_subdirectory + 'raw.json', 'w') as f:
#         json.dump(raw_data, f, indent=4, sort_keys=True)
    
#     with open(name_data_subdirectory + 'dictionary.json', 'w') as f:
#         json.dump(string_dictionary_data, f, indent=4, sort_keys=True)

dataDir = r'C:\Users\thepe_000\Desktop\PP5\Void-Web\Enviorment\data\nametypes'
from DataIndex import DataIndex
DI = DataIndex(dataDir)

targeted = []
for nameType in DI.keys():
    if 'placeName' in nameType or 'Forenames' in nameType or 'Surnames' in nameType:
        DI[nameType].Proper = True
    else:
        targeted.append(nameType)

for nameType in targeted:
    print(nameType)
    inp = ''
    while inp not in ['y', 'n']:
        inp = input()
    if inp == 'y':
        DI[nameType].Proper = True