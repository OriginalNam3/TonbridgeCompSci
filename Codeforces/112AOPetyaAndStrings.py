# https://codeforces.com/problemset/problem/112/A

a = input()
b = input()
a = a.lower()
b = b.lower()

l = 'abcdefghijklmnopqrstuvwxyz'

for i, j in zip(a, b):
    if i != j:
        print(2*(l.index(i) > l.index(j)) - 1)
        exit(0)
print(0)