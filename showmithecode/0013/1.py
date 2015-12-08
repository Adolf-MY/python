#coding=utf8
__author__ = 'Frank'
import os,urllib
from bs4 import BeautifulSoup
from urlparse import urlsplit

url = 'http://tieba.baidu.com/p/2166231880'
content = urllib.urlopen(url)
#print content
bs = BeautifulSoup(content,'lxml')
for i in bs.find_all('img',{'class':'BDE_Image'}):
    url1 = i['src']
    image_content = urllib.urlopen(url1).read()
    file_name = os.path.basename(urlsplit(url1)[2])
    '''a = []
    a.append(urlsplit(url1)[2])
    print a[0].split('=')[1]'''
    path = 'E:/python/Users/Frank/PycharmProjects/python/python/showmithecode/0013/'+file_name
    output = open(path,'wb')
    output.write(image_content)
    output.close()