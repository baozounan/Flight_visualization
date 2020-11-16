from utils.convert import *
import json
def appendCsvData(data):
   data1=str(123.78)
   file=open("panel_test_data.csv","r+",newline="")
   reader = csv.reader(file)
   print(list(reader))
   original = list(reader)
   print(original)
   content = csv.writer(file)
   for row in original:
       content.writerow(row)
   content.writerow(data1)
   file.close()
   return

if __name__ == '__main__':
    appendCsvData(12)