import os
import numpy as np
import re

'''
提取输出数据集（program）方法
每一class带领一系列method
'''

'''
形如
public class AgelessEntity extends CardImpl {
public AgelessEntity(UUID ownerId) {
public AgelessEntity(final AgelessEntity card) {
public AgelessEntity copy() {return new AgelessEntity(this);
class AgelessEntityEffect extends OneShotEffect {
public AgelessEntityEffect() {
public AgelessEntityEffect(final AgelessEntityEffect effect) {
public AgelessEntityEffect copy() {return new AgelessEntityEffect(this);
public boolean apply(Game game, Ability source) {return new AddCountersSourceEffect(CounterType.P1P1.createInstance(lifeGained)).apply(game, source);return false;
public class AgonizingDemise extends CardImpl {
public AgonizingDemise(UUID ownerId) {
public AgonizingDemise(final AgonizingDemise card) {
public AgonizingDemise copy() {return new AgonizingDemise(this);

'''

# 读文件
filename = './data/program.txt'
with open(filename, 'rb') as f:
    content = f.read().decode('utf-8')

lines = content.split("\n")
temp = []
return_line = ""
method_line = ""
# count = -1

# 数据集特点：
for i in lines:
    # if ";" not in i and "if" not in i and "while" not in i and "}" not in i and "for" not in i and "static" not in i and "this" not in i and "{" in i and "." not in i and "switch" not in i and "do" not in i and "else" not in i and "try" not in i and "catch" not in i and "finally" not in i:
    method_line = i.split('$')[0]
    temp.append(method_line)
        # count += 1
    # elif "return" in i:
    #     return_line = str(i)
    #     temp[count] += return_line

temp = list(filter(None, temp))
method = []
for i in temp:
    # print(i)
    if len(str(i)) >= 2:
        method.append(i)

# 写之前，先检验文件是否存在，存在就删掉
filename2 = "./data/all_method.txt"
if os.path.exists(filename2):
    os.remove(filename2)

# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open(filename2, 'w')
for var in method:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

for i in temp:
    print(i)
