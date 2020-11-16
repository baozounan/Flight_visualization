import pandas as pd
import csv
import openpyxl
import numpy
def str2dict(str):

    """将str类型转换成字典类型，输入一个字符串，返回一个字典"""

    dict = exec(str)
    return

def savedata2xlsx(data):
    """将data保存为本地xlsx文件"""
    new = openpyxl.load_workbook("E:\\test_data\\test.xlsx")  # 加载文件
    sheet = new.create_sheet(title="sheet_title")
    for row in range(len(data)):  # len(use_data)
       # len(use_title)
         _ = sheet.cell(row=row + 1, column=1, value=u'%s' % data[0][row])
    newexcel = new.save("E:\\test_data\\test.xlsx")

def appendCsvData(data):

   file=open("data\\panel_test_data.csv","a+",newline="")
   reader = csv.reader(file)
   original = str(reader)
   content = csv.writer(file)
   for row in original:
       content.writerow(row)
   content.writerow(data)
   file.close()
   return






