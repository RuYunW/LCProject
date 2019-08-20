import os

# 读文件
filename = 'train_magic_method_class.txt'
with open(filename, 'rb') as f:
    content = f.read().decode('utf-8')

content = content.split("\n")
flag = []

for i in content:
    if "class" in i:
        flag.append(1)
    else:
        flag.append(0)

temp = []
class_name = ""

for i in range(len(flag)):
    if flag[i] == 1:
        class_name = content[i]
    elif flag[1] == 0:
        method = class_name.replace("\r","") + content[i]
        # print(method)
        temp.append(method)

# 写之前，先检验文件是否存在，存在就删掉
if os.path.exists("train_magic_class_method2.txt"):
    os.remove("train_magic_class_method2.txt")

# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open("train_magic_class_method2.txt", 'w')
for var in temp:
    file_write_obj.writelines(var)
    # file_write_obj.write('\n')
file_write_obj.close()

