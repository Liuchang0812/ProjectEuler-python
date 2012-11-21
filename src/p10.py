__author__ = 'liuchang'
import math
def isp(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True


lm = 2000000
pm = 0
for i in range(2,lm+1):
    if isp(i):
        pm = pm + i
print pm
