n = int(input())

colours = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

print('BIVROYG', end='') # print all colours so the condition is fulfilled.
n -= 7
for i in range(n // 4):
    for j in range(4):
        print(colours[j], end='')
for i in range(n%4):
    print(colours[i], end='')
# Just keep cycliing through four colours as the three colours at the beginning will not be the same as 
