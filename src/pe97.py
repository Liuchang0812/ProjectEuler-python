__author__ = 'liuchang'

ans = 1
for i in range(7830457):
    ans = ans * 2
    ans = int(str(ans)[-10:])
    # print "%d : %d " % ( i , ans )

print str(ans *  28433 + 1)[-10:]