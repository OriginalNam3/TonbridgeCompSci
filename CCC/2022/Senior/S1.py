n = int(input())
# Consider number of fours in the sum
# If n % 4 <= n // 4, each unit in remainder contributes to a four which forms a five, and u consider how many groups of five fours there are.
print((n//4 - n%4)//5 + 1 if n//4 >= n%4 else 0) 
