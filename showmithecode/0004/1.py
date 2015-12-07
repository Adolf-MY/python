__author__ = 'Frank'
# -*- coding: utf-8 -*-
import re
def count(path):
    f = open(path,'rb')
    s = f.read()
    w = re.findall(r'[a-zA-z0-9]+',s)
    return len(w)

if __name__ == '__main__':
    num = count('E:/python/Users/Frank/PycharmProjects/python/showmithecode/0004/a.txt')
    print(num)




