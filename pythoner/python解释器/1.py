#coding=utf8
__author__ = 'Frank'
def foo(x):
    a=3
    return a+x
#print foo
#print foo.func_code
#print dir(foo.func_code)
#print foo.func_code.co_varnames
#print foo.func_code.co_consts
#print foo.func_code.co_argcount
#print foo.func_code.co_code
print [ord(b) for b in foo.func_code.co_code]
import dis
dis.dis(foo.func_code)