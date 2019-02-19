import os
from void_scribe.data import Stories

f = open("sentencelist.txt", "a")

for name in Stories.data.keys():
    f.write(str(name)+'\n')