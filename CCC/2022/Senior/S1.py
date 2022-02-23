n = int(input())

fours = n // 4
remainder = n % 4

# Each unit in remainder can be distributed to a four in the sum to make it a five
# So we just have to check how many groups of five fours there are in the fours (as they can be made into groups of four fives)

print((fours - remainder)//5 + 1 if fours >= remainder else 0) 
