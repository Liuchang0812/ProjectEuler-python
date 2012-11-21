__author__ = 'liuchang'

maxn = -1
def ispali(x):
    s = str(x)
    #print "%d %s"%(x,s)

    i = 0
    j = len(s) - 1
    #print "%d %d"%(i,j)
    while s[i] == s[j] and i < j:
        i = i+1
        j = j-1
    if i >= j:
        return True
    return False

for a in range(100,1000):
    for b in range(100,1000):
        if ispali(a*b):
            maxn = max(maxn,a*b)
print maxn
