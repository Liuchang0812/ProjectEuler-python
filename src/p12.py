__author__ = 'liuchang'


def how(x):
    i = 1
    ans = 0
    while i*i <= x:
        if x % i == 0:
            ans = ans + 1
            if i *i != x:
                ans = ans + 1
        i = i + 1;
    return ans

st = 1
tri_num = 1
while how(tri_num) <= 500:
    print st,tri_num
    st = st + 1
    tri_num = tri_num + st

print tri_num
