# You are opening a small pizzeria. In fact, your pizzeria is so small that you decided to offer only one type of pizza. Now you need to decide what ingredients to include (peppers? tomatoes? both?).

# Everyone has their own pizza preferences. Each of your potential clients has some ingredients they like, and maybe some ingredients they dislike. Each client will come to your pizzeria if both conditions are true:

# all the ingredients they like are on the pizza, and
# none of the ingredients they dislike are on the pizza
# Each client is OK with additional ingredients they neither like or dislike being present on the pizza. Your task is to choose which ingredients to put on your only pizza type, to maximize the number of clients that will visit your pizzeria.

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
