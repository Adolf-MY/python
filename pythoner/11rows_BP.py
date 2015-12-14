#coding=utf8
__author__ = 'Frank'
import numpy as np
def nonlin(x,deriv = False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])#4*3
y = np.array([[0],[1],[1],[0]])#4*1
np.random.seed(1)
syn0 = 2 * np.random.random((3,4))-1#3*4
syn1 = 2 * np.random.random((4,1))-1#4*1
for i in range(10000):
    l0 = x#4*3
    l1 = nonlin(np.dot(l0,syn0))#4*4
    l2 = nonlin(np.dot(l1,syn1))#4*1
    l2_error = y - l2#4*1
    if (i%1000)==0:
        print "Error" + str(np.mean(np.abs(l2_error)))
    print l1.size()
    l2_delta = nonlin(l1,True)*l2_error#4*1
    print l2_delta.shape
    l1_error = np.dot(l2_delta,syn1)#4*4
    l1_delta = l1_error*nonlin(l1,True)#4*4
    syn1 += np.dot(l1.T,l2_delta)
    syn0 += np.dot(l0.T,l1_delta)
print "Output After Training"
print l2


