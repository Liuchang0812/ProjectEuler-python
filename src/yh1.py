__author__ = 'liuchang'

n = int(raw_input())
for cs in range(n):
    a , b , m , d  = (raw_input().split(' '))
    a = int(a)
    b = int(b)
    m = int(m)
    d = int(d)

    now_pos = 1
    count = 0
    occur = {}
    a = a % b
    ans = ''
    while True:
        a = a * 10
        k = a / b
        a = a % b

        print k , a
        if a == d:
            count += 1
            if count == m:
                print now_pos
                break

        if a == 0:
            print 0
            break
        if occur.has_key(a):

            break

        occur[a] = now_pos
        now_pos += 1
        ans += chr(a + ord('0'))