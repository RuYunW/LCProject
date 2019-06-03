import os
import numpy as np
import re

# 读文件
filename = 'train_magic.txt'
with open(filename, 'rb') as f:
    content = f.read().decode('utf-8')

# 按行分割
content = content.split("\n")

# 清洗
