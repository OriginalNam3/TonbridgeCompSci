# https://codeforces.com/problemset/problem/534/A

n = int(input())

a = []
# Odd numbers in descending order, then even numbers in descending order
for i in range(n - (not (n % 2)), 0, -2):
    a.append(i)
for i in range(n - (n % 2), 0, -2):
    a.append(i)

if n == 2: # The only case where the above does not work is n = 2 where a = [1, 2]
    a.pop(-1)

print(len(a))
for i in a:
    print(i, end=' ')
