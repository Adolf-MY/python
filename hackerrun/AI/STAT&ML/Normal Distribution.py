#coding=utf8
__author__ = 'Frank'
import sys
from scipy import stats
for i in range(1):
    line = sys.stdin.readline()
    print line
    line1 = line.split()
    print line1
    pjs =int(line1[0])
    bzc = int(line1[1])
    print pjs,bzc
X = stats.norm(loc= pjs,scale = bzc)
a = [0 for i in range(3)]
a[0] = round(X.cdf(40),3)
a[1] = round(X.cdf(pjs+(pjs-21)),3)
a[2] = round(X.cdf(35)-(1-X.cdf(pjs)),3)
print a
for i in range(3):
    sys.stdout.write('%.3f\n'%a[i])
    sys.stdout.flush()
    #print a[i]