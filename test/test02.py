# -*- coding:utf-8 -*-
import xlwings as xw

list1 = [[1],[2],[3],[4],[5]]
sht = xw.Book().sheets('sheet1')  # 新增一个表格
sht.range('A1').value = list1