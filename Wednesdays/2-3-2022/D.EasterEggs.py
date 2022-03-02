n = int(input())

colours = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

print('BIVROYG', end='') # print all colours so the condition is fulfilled
n -= 7
# Now we have to make sure that four sequential eggs are the same colour
# This can simply be done by looping through the four colours at the end of the first seven colours printed
for i in range(n):
    print(colours[i % 4], end='')
# Note that because the first three colours are never used within the cycle
# Therefore, no matter what colour you end on, the first three colours at the beginning and the colour at the end will not overlap
