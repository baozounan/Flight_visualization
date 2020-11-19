# -*- coding:utf-8 -*-
import xlwings as xw
import numpy as np
"""orderIds = [1.2,2.4,3.6]
items = [12.33,12.45,34.56]
myData = [10.66,20.77,30.88]
testData = [orderIds,items,myData]
print(testData)
print(len(testData)) # 行数
print(len(testData[0])) # 列数
print(testData[1][2]) #二维数组行列下表
data=np.transpose(testData).tolist()
print(data)
data=np.array(data)
clo_data=data[:,1]
print(clo_data)"""
a=[[1,2,3], ['1952.11','34.56','45.67']]
a=np.array(a)
for i in range(len(a)+1):
    b=a[:,i]
    print(b)