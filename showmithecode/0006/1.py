#coding=utf8
__author__ = 'Frank'
import sys
import os
import re
sys.path.append('E:/python/Users/Frank/PycharmProjects/python')
from showmithecode.xiexian import change_xiexian as aaa
path = r'E:\python\Users\Frank\PycharmProjects\python\showmithecode\0006\note'
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
def get_important_word(files):
    worddict ={}
    for filename in files:
        #print filename
        f = open(filename,'rb')
        s = f.read()
        words = re.findall(r'[a-zA-Z0-9]+',s)
        #print words
        for word in words:
            worddict[word] = worddict[word]+1 if word in worddict else 1
        f.close()
    #print worddict
    wordsort = sorted(worddict.items(),key = lambda e:e[1],reverse = True)
    return wordsort

if __name__ =='__main__':
    files = getfile(path1)
    #print files
    wordsort = get_important_word(files)
    print wordsort