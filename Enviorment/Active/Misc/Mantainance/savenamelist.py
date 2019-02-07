import names as nms

names = list(nms.names.keys())

with open('name_type_list.txt',"w+") as f:
    for name in names:
        f.write(name + '\n')

test = {
"american" : {}


}