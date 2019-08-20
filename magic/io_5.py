from openpyxl import load_workbook, Workbook
from collections import Counter
import os
import re

# 读文件
filename = 'train_magic_class_name3.txt'
with open(filename, 'rb') as f:
    content = f.read().decode('utf-8')
content = content.replace("\r","").replace("\n","").replace(str(re.findall()))
content = content.split(":")
# print(content)

new_name = []
for i in content:
    for j in range(Counter(content)[i]):
        new_name.append(i+"_"+str(j))

# 写之前，先检验文件是否存在，存在就删掉
if os.path.exists("train_magic_new_name5.txt"):
    os.remove("train_magic_new_name5.txt")

# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open("train_magic_new_name5.txt", 'w')
for var in new_name:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

