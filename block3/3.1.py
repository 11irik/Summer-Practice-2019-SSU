import math

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

a = int(input())

sum = 0
factor = 1
k = 1
while sum < a:
    k += 3
    factor *= k
    sum += factor
print(sum - factor)

