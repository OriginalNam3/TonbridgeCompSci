# https://codeforces.com/problemset/problem/285/A

n, k = map(int, input().split())

p = list(range(1, n-k)) + list(range(n, n-k-1, -1))
for n in p:
    print(n)