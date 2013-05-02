__author__ = 'liuchang'
'''
    1
    3 5 7 9           2
    13 17 21 25       4
    31 37 43 49       6
'''



ans , now , add = 1 , 3 , 2
for i in range(500):
    for j in range(4):
        print now
        ans = ans + now
        now = now + add
    now = now + 2
    add = add + 2

print ans
