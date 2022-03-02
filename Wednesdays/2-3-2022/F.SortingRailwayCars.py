n = int(input())

# The essence of this problem is to find the longest ordered range of numbers
# This means we need to find the longest [a, a + 1, a + 2, ... , b -1, b] in the given array
# This is because we can simply move any numbers less than a and larger than b to the front and the back in order
# Note that any number less than a or larger than b can be between a and b as long as every number between a and b is in sorted order between them

p = list(map(int, input().split()))
a = [0] * (n+1)
for i in range(n):
    a[p[i]] = a[p[i]-1] + 1  
    # The length of the ordered range up to p[i] is given by the length of the ordered range up to (p[i] - 1) at that point
    # This is known as dynamic programming
print(n - max(a))
