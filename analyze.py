import os
import numpy as np
import re

# 读文件
filename = 'train_magic.txt'
with open(filename, 'rb') as f:
    content = f.read().decode('utf-8')

lines = content.split("\n")
temp = []
for i in lines:
    if ";" not in i and "if" not in i and "while" not in i and "}" not in i and "for" not in i and "static" not in i and "this" not in i and "{" in i and "." not in i and "switch" not in i and "do" not in i and "else" not in i:
        temp.append(i)

temp = list(filter(None, temp))
method = []
for i in temp:
    if len(str(i))>=2:
        method.append(i)

for i in range(len(method)):
     method[i].replace(" ","")

for i in method:
    if "public" not in i and "class" not in i:
        print(i)

# 写之前，先检验文件是否存在，存在就删掉
if os.path.exists("train_magic_method_class.txt"):
    os.remove("train_magic_method_class.txt")

# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open("train_magic_method_class.txt", 'w')
for var in method:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

