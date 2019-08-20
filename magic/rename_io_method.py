import os
import re


with open('train_magic_class_method_io3.txt','rb') as f1:
    old = f1.read().decode('utf-8')
with open('magic_new_name2.txt','rb') as f2:
    new_name = f2.read().decode('utf-8')

old = old.split('\n')
new_name = new_name.split('\n')
# print(len(new_name))
# print(len(old))

name = []
other = []
for i in range(len(old)):
    other.append(old[i].replace(old[i].split('-')[0],""))

if os.path.exists("magic_final_result.txt"):
    os.remove("magic_final_result.txt")

file_write_obj = open("magic_final_result.txt", 'w')
for i in range(len(old)):
    file_write_obj.writelines(new_name[i].replace('\r','')+other[i])
    # file_write_obj.write('\n')
file_write_obj.close()