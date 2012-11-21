s = 2**1000
s = str(s)
ans = 0
for i in range(len(s)):
    ans = ans + ord(s[i]) - ord('0')
print ans
