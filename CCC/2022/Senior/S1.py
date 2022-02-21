n = int(input())

fours = n // 4
remainder = n % 4

if fours >= remainder: # Each unit in remainder can be attributed to a four in the sum to make it a five
    print((fours - remainder)//5 + 1) # Check how many groups of five fours there are in the fours (as they can be made into groups of four fives)
else:
    print(0)
