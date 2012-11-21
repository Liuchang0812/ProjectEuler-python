__author__ = 'liuchang'
limit = 4000000
a,b = 1,2
sum = 2;
while b <= limit:
    a,b = b,a+b
    if b % 2 == 0:
        sum = sum + b
print sum