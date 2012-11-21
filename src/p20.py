s = 1
for i in range(1,101):
    s = s * i
s = str(s)
ans = 0
for i in s:
    ans = ans + ord(i) - ord('0')
print ans
