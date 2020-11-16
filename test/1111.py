# encoding:utf-8
import xlsxwriter as xw
import pandas as pd
import openpyxl as op
orderIds = [1.2,2.4,3.6]
items = ['A','B','C']
myData = [10.66,20.77,30.88]
testData = [orderIds,items,myData]

filename1 = 'panel_test_data.csv'

def xw_toexcel(data,filename): # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(filename) # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1") # 创建子表
    worksheet1.activate() # 激活表
    title = ['序号','项目','数据'] # 设置表头
    worksheet1.write_row('A1',title) # 从A1单元格开始写入表头
    i = 2 # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[0][j],data[1][j],data[2][j]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close() # 关闭表
    return None

xw_toexcel(testData,filename1)