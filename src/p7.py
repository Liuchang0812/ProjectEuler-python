__author__ = 'liuchang'

from math import sqrt,ceil





def ispm(x):
    i = 2
    while i*i<=x:
        if x % i == 0:
            return False;
        i = i + 1
    return True;
st = 2;
ret = 0;
print ispm(5)
while True:
    if ispm(st):
        ret = ret + 1
        if ret == 10001:
            print st
            exit
    st = st + 1


