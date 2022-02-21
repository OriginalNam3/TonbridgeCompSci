# Doesn't work for the very last test case in the last subtask

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


def search(start, end, last):
    if start == end:
        return start
    mid = (start + end) // 2
    t = get_time((start + mid) // 2)
    if t < last:
        return search(start, mid, t)
    t = get_time((mid + end) // 2)
    if t < last:
        return search(mid, end, t)
    if abs(end - start) == 1:
        st = get_time(start)
        et = get_time(end)
        if st == et: return start
        if st < et: return start
        else: return end
    return search((start + mid) // 2, (mid + end) // 2, last)


print(get_time(search(min(p), max(p), get_time((min(p) + max(p))//2))))
