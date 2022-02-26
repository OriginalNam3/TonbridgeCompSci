x = int(input())
together = []
for _ in range(x):
    together.append(input().split())
y = int(input())
separate = []
for _ in range(y):
    separate.append(input().split())
at_group = {}
g = int(input())
for i in range(g):
    grp = input().split()
    for k in grp:
        at_group[k] = i

cnt = 0
for rule in together:
    if at_group[rule[0]] != at_group[rule[1]]: cnt += 1
for rule in separate:
    if at_group[rule[0]] == at_group[rule[1]]: cnt += 1
print(cnt)
