__author__ = 'liuchang'

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def gcm(a,b):
    return a / gcd(a,b) * b

ans = gcm(1,2)
for i in range(2,21):
        ans = gcm(ans,i)
print ans
