# https://codeforces.com/problemset/problem/110/A

def islucky(s):
    for n in s:
        if n != '4' and n != '7':
            return False
    return True

s = input()
if islucky(s):
    print('YES')
    exit(0)
if islucky(str(s.count('4') + s.count('7'))):
    print('YES')
    exit(0)
print('NO')