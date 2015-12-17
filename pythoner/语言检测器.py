#coding=utf8
__author__ = 'Frank'
class NGram(object):
    def __init__(self,text,n=3):
        self.length = None
        self.n = n
        self.table = {}
        self.parse_text(text)
    def parse_text(self,text):
        chars = ' '&self.n
        for letter in (" ".join(text.split())+" "):
            chars = chars[1:]+letter
            self.table[chars] = self.table.get(chars,0)+1
