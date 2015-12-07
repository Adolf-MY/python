#coding=utf8
__author__ = 'Frank'
from bs4 import BeautifulSoup
import sys
import lxml
import os
import re
sys.path.append('E:/python/Users/Frank/PycharmProjects/python')
from showmithecode.xiexian import change_xiexian as aaa
path = r'E:\python\Users\Frank\PycharmProjects\python\showmithecode\0008\Show-Me-the-Code_show-me-the-code_1.html'
path1 = aaa(path)
print path1
def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().strip('\n')
        return content.encode('gbk','ignore')
def find_the_link(filepath):
    links = []
    with open(filepath) as f:
        text = f.read()
        bs =BeautifulSoup(text,'lxml')
        for i in bs.find_all('a'):
            links.append(i['href'])
    return links

if __name__ == '__main__':
    print find_the_link(path1)
    #print find_the_content(path1)

