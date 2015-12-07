#coding=utf8
__author__ = 'Frank'
import sys
import os
import re
sys.path.append('E:/python/Users/Frank/PycharmProjects/python')
from showmithecode.xiexian import change_xiexian as aaa
path = r'E:\python\Users\Frank\PycharmProjects\python\showmithecode\0007'
path1 = aaa(path)
def getfile(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path+ '/' + fp
        if(os.path.isfile(fppath)):
            files.append(fppath)
        elif(os.path.isdir(fppath)):
            files += getfile(fppath)
    return files
def count_lines(files):
    line,block,note = 0,0,0
    for filename in files:
        f = open(filename,'rb')
        for l in f:
            l= l.strip()
            line += 1
            if l=='':
                block +=1
            elif l[0]=='#' or l[0]=='/':
                note +=1
        f.close()
    return(line,block,note)
if __name__=='__main__':
    files = getfile(path1)
    print files
    lines =count_lines(files)
    print lines