# https://codeforces.com/problemset/problem/1325/A
t = int(input())

# gcd(1, x-1) = 1
# lcm(1, x-1) = x-1
# gcd + lcm = 1 + x - 1 = x

for _ in range(t):
    x = int(input())
    print(1, x-1)
