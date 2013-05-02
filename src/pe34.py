__author__ = 'liuchang'

def fact(x):
    ans = 1
    for i in range(1,x+1):
        ans = ans * i
    return ans

def f(x):
    return sum( [ fact(ord(i) - ord('0')) for i in str(x)] )

ans = set()

for i in range(3 , 10000000):
    if i == f(i):
        ans.add(i)
print sum(ans)
