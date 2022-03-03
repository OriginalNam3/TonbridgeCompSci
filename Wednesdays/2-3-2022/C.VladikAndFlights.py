# https://codeforces.com/problemset/problem/743/A

n, a, b = map(int, input().split())

# Because there are only two companies, there has to be an airport where the two companies are right next to each other.

s = list(map(int, [c for c in input()]))

print(1 if s[a-1] != s[b-1] else 0)
