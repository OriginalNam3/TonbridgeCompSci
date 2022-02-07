c = int(input())
d = []
g = [[] for i in range(c)]

for i in range(c):
    l = input().split()[1:]
    dl = input().split()[1:]
    d.append([l, dl])

for i in range(c):
    print(i)
    l, dl = d[i]
    for j in range(len(d)):
        if [k for k in l if k in d[j][1]] or [k for k in dl if k in d[j][0]]:
            g[i].append(j)
# c = 10
# d = [[[i], []] for i in range(10)]
# g = [[5, 6, 7, 9], [2, 6, 7], [], [8], [0, 2, 7, 9], [0, 1, 8], [0, 1, 5], [4, 6, 9], [0, 2, 5, 8]]


h = [len(lst) for lst in g]

while True:
    m = h.index(min(i for i in h if i > 0))
    ng = g[m]
    for i in ng:
        print(i)
        d[i] = [[], []]
        g[i] = []
        for k in g:
            if i in k: k.remove(i)
    h = [len(lst) for lst in g]
    print(len(d))
    print(sum(h))
    if sum(h) == 0:
        break

i = set([])
for l, _ in d:
    for ing in l:
        i.add(ing)
i = list(i)
s = str(len(i)) + ' '
for ing in i:  s += ing + ' '
print(s)



#     print(len(d))
#     for e in d:
#         if not [i for i in l if i in e[2]] and not [i for i in dl if i in e[1]]:
#             d.append([e[0] + 1, e[1] + [i for i in l if i not in e[1]], e[2] + [i for i in dl if i not in e[2]]])
#     d.append([1, l, dl])
#     d.sort()
#
# ic = [e[0] for e in d]
# i = d[ic.index(max(ic))][1]
# s = str(len(i)) + ' '
# for ing in i:  s += ing + ' '
# print(s)