from void_scribe import NamesDictionary

nd = NamesDictionary.NamesDictionary()
names = nd.keys()

with open('name_type_list.txt',"w+") as f:
    for name in names:
        f.write(name + '\n')
