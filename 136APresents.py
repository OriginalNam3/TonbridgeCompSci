# https://codeforces.com/problemset/problem/136/A

n = int(input())
i = [0] * n
p = list(map(int, input().split()))

for x in range(len(p)):
    i[p[x]-1] = x+1

for j in i:
    print(j)
