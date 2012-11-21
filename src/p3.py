__author__ = 'liuchang'
lm = 600851475143
ans = -1
import math
def isp(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

pm = set()
for i in range(2,int(math.sqrt(lm))+1):
    if isp(i):
        pm.add(i)
for i in pm:
    print i
    if lm % i == 0:
        ans = i
print ans


