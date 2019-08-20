from collections import Counter
import os
with open('train_magic_class_method_io3.txt','rb') as f:
    content = f.read().decode('utf-8')
content = content.split("\n")
new_name = []
for i in content:
    item = i.split("-")[0]
    new_name.append(item)

new_name2 = list(set(new_name))
new_name2 = list(filter(None, new_name2))
temp = []
for i in new_name2:
    for j in range(Counter(new_name)[i]):
        temp.append(i+"_"+str(j))

if os.path.exists("magic_new_name2.txt"):
    os.remove("magic_new_name2.txt")

file_write_obj = open("magic_new_name2.txt", 'w')
for var in temp:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()