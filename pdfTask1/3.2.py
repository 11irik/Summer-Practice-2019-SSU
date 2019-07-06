import math

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#Воозможно потерял данные
a = []
k = int(input())
max = k

while k != 0:
    k = int(input())
    if max < k:
        max = k

print(max)