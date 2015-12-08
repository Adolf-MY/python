#coding=utf8
__author__ = 'Frank'
import os,json,xlwt,pandas
with open(os.path.join(os.path.split(__file__)[0],'city.txt'),'r') as f:
    text = f.read().decode('utf-8')
    text_json = json.loads(text)

wb = xlwt.Workbook()
ws = wb.add_sheet('city',cell_overwrite_ok=True)
row = 0
col = 0
for k,v in sorted(text_json.items(),key = lambda d:d[0]):
    ws.write(row,col,k)
    col +=1
    ws.write(row,col,v)
    row +=1
    col =0
wb.save('city.xls')