#coding=utf8
__author__ = 'Frank'

#type_in = raw_input(">")
judge_flag = False
path = r'E:\python\Users\Frank\PycharmProjects\python\python\showmithecode\0011\filtered_words.txt'
path1 = path.replace('\\\\','/')
with open(path1) as f:
    text = f.read()
#for i in text.split('\n'):
#    if i in type_in:
#        judge_flag = True
#if judge_flag:
#    print 'Freedom'
#else:
#    print 'Human Rights'
for i in text.split('\n'):
    if i in type_in:
        a = type_in.replace(i,''.join(['*' for j in range(len(i))]))
print a
