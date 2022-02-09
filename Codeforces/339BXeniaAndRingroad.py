# https://codeforces.com/problemset/problem/339/B

n, m = map(int, input().split())

a = list(map(int, input().split()))
t = 0
pos = 1
for i in a:
    t += (i-pos) % n
    pos = i
print(t)