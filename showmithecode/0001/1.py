# -*- coding:utf-8 -*-
__author__ = 'Frank'
import random,string,pandas
def rand_str(n,m):
    f = []
    for i in range(n):
        chars = string.digits+string.letters
        s = [random.choice(chars) for i in range(m)]
        f.append(''.join(s))
        f1 = pandas.DataFrame(f)
    return f1
#print rand_str(200,7)