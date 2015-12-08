#coding=utf8
__author__ = 'Frank'
import re,os,json,xlwt,pandas
#path = '‪E:/python/Users/Frank/PycharmProjects/python/python/showmithecode/0014/student.txt'
with open(os.path.join(os.path.split(__file__)[0],'student.txt'),'r') as f:
    text = f.read().decode('utf-8')
    text_json = json.loads(text)
wb = xlwt.Workbook()
ws = wb.add_sheet('student',cell_overwrite_ok=True)
row = 0
col = 0
for k,v in sorted(text_json.items(),key = lambda d:d[0]):
    ws.write(row,col,k)
    for i in v:
        col +=1
        ws.write(row,col,i)
    row +=1
    col =0
wb.save('student.xls')