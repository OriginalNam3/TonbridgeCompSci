# https://codeforces.com/problemset/problem/96/A

s = input()

for i in range(0, len(s)-6):
    if s[i: i+7] == '1111111' or s[i: i+7] == '0000000':
        print('YES')
        exit(0)
print('NO')