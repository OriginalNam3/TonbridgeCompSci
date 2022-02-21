d = {}
for p in range(2):
    x = int(input())
    for _ in range(x):
        a, b = input().split()
        if a not in d:
            d[a] = [[], []]
        if b not in d:
            d[b] = [[], []]
        d[a][p].append(b)
        d[b][p].append(a)


c = 0
g = int(input())
for _ in range(g):
    group = input().split()
    for i in range(3):
        if group[i] in d:
            v = [[], []]
            for p in d[group[i]][0]:
                if p not in group:
                    v[0].append((group[i], p))
                    c += 1
            for j in range(i+1, 3):
                if group[j] in d[group[i]][1]:
                    v[1].append((group[i], group[j]))
                    c += 1
            for vi in range(2):
                for a, b in v[vi]:
                    d[a][vi].remove(b)
                    d[b][vi].remove(a)
print(c)
