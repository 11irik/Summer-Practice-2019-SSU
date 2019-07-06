import sys
import numpy as np

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

l = [['A', 'B', 'C'],
     ['B', 'C', 'A'],
     ['C', 'A', 'B']]

a = np.array(l)
n = int(input())
x, y = map(int, input().split())
print(a, '\n')

while n > 1:
    a = np.concatenate((a, np.fliplr(a)), axis=1)
    a = np.concatenate((a, np.flipud(a)), axis=0)
    n //= 2

print(a, '\n')

print(a[x, y])