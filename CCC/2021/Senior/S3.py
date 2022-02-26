n = int(input())
p = []
w = []
d = []

for _ in range(n):
    np, nw, nd = list(map(int, input().split()))
    p.append(np)
    w.append(nw)
    d.append(nd)


def get_time(c):
    d_ = [abs(p[i]-c) - d[i] if d[i] < abs(p[i]-c) else 0 for i in range(n)]
    t = sum(d_[i] * w[i] for i in range(len(w)))
    return t


def search(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    lt = get_time(mid-1)
    rt = get_time(mid+1)
    if lt < rt:
        return search(start, mid)
    if rt < lt:
        return search(mid, end)
    if lt == rt: return mid


print(get_time(search(min(p), max(p))))
