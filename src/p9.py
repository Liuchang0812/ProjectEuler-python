__author__ = 'liuchang'

for a in range(400):
    for b in range(a,400):
        c = 1000 - a - b
        if c > b and c > a and a*a + b*b == c*c:
            print "%d %d %d"%(a,b,c)
            print a*b*c
            exit