# полиномиальный хэш
p = 31
m = 10**9
DIC_START = ord('a') - 1

def get_hash(l, r):
    if l == 0:
        return h[r]
    return (h[r] - (h[l - 1] * powp[r - l + 1]) % m + m) % m

s = input()
h = [0 for _ in range(len(s))]
h[0] = ord(s[0]) - DIC_START
powp = [0 for _ in range(len(s))]
powp[0] = 1
for i in range(1, len(s)):
    h[i] = (p * h[i - 1] + ord(s[i]) - DIC_START) % m
    powp[i] = (powp[i - 1] * p) % m

ans = []
n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if get_hash(a - 1, b - 1) == get_hash(c - 1, d - 1):
        ans.append('Yes')
    else:
        ans.append('No')

print(*ans, sep = "\n")