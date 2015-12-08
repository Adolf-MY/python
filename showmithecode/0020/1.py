#coding=utf8
__author__ = 'Frank'
import xlrd
import datetime,time
import os,re
path = os.path.join(os.path.split(__file__)[0],r'2015年11月语音通信.xls')
path1 = unicode(path,'utf-8')
info_file = xlrd.open_workbook(path1)
info_table = info_file.sheets()[0]
row_count = info_table.nrows
infos=[]
#print row_count
for row in range(7,row_count):
    time_string = info_table.cell(row,2).value
    #print time_string
    time_s_sp = re.split(':|-| ',time_string)
    #print time_s_sp
    infos.append(
        {
            'type':info_table.cell(row,4).value,
            'number':info_table.cell(row,5).value,
            'timespan':datetime.timedelta(
                seconds=int(time_s_sp[5]),
                minutes=int(time_s_sp[4]),
                hours=int(time_s_sp[3])),
            'class':info_table.cell(row,7).value
        }
    )
time_all = datetime.timedelta(seconds=0)
time_types = {}
time_classes = {}
time_numbers = {}
for infor in infos:
    time_all += infor['timespan']

    infor_type = infor['type']
    if infor_type in time_types:
        time_types[infor_type] += infor['timespan']
    else:
        time_types[infor_type] = infor['timespan']

    infor_class = infor['class']
    if infor_class in time_classes:
        time_classes[infor_class] += infor['timespan']
    else:
        time_classes[infor_class] = infor['timespan']

    infor_number = infor['number']
    if infor_number in time_numbers:
        time_numbers[infor_number] += infor['timespan']
    else:
        time_numbers[infor_number] = infor['timespan']


print '总通话时间：%s' % time_all
print
print '通信方式分类：'
for (k, v) in time_types.items():
    print k.encode('utf-8'), v
print
print '通信类型分类：'
for (k, v) in time_classes.items():
    print k.encode('utf-8'), v
print
print '对方号码分类：'
for (k, v) in time_numbers.items():
    print k.ljust(20), v