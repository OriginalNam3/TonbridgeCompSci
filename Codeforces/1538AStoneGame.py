# https://codeforces.com/contest/1538/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mi = a.index(min(a)) + 1  # Getting index of minimum element in array
    ma = a.index(max(a)) + 1  # Getting index of maximum element in array
    # Note that mi and ma are exchangeable as long as we use min and max functions to make sure we know which one is on which side
    # Therefore, we shall simply call them m
    # There are three cases:
    # 1. [ ..., m, ... , m, ..., ..., ...] so we go -> -> 
    # 2. [ ... ... ..., m, ... , m, ...]  the opposite: <- <-
    # 3. [ ..., m, ... ... ... , m, ...] this time it goes -> + <-
    print(min([abs(mi - ma) + min(mi, ma), min(mi, ma) + n - max(ma, mi) + 1, abs(mi - ma) + n - max(mi, ma) + 1]))  # find min of all three cases
    
