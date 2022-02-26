import math
n, circumference = map(int, input().split())
global h
h = math.ceil(circumference / 2)
d = [0] * circumference
plst = list(map(int, input().split()))
for p in plst:
    d[p] = 1

d = d * 2
s = sum(d[0: h])
c = 0
for p in d[:n]:
    c += math.comb(s, 2)
    s -= d[p]
    s += d[p+h]
c = math.comb(n, 3) - c
print(c)
