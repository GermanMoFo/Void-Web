import os
from void_scribe import NameGenerator

f = open("namelist.txt", "a")

for name in list(NameGenerator.getNameTypes()):
    f.write(str(name)+'\n')