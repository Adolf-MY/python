#coding=utf8
__author__ = 'Frank'
import time
a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
b = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+60*60*9))
f = open('C:\Users\Frank\Desktop\signin.txt','w')
f.write(a+'\n')
f.write(b+'\n')
f.close()