import numpy as np
from openpyxl import Workbook
wb = Workbook()
ws = wb.worksheets[0]
ws.title = 'sheet1'
ws.cell(row=1, column=1).value = '库存药剂信息概览报表'
wb.save(filename = "666.xlsx")
# a = [1, 1, 3]
# b = [4, 5, 5]
# # print(a.index(2))
# matrix = np.ones((3, 3))
# matrix[1][1] = 0
# print(matrix)

