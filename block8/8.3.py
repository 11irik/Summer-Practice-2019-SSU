import numpy as np
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = map(int, (input().split()))

vec = np.random.randint(10, size=n)
arr = np.random.randint(10, size=n*m).reshape(n,m)
endArr = np.copy(arr)
print(vec)
print(arr)

maxinvec = np.max(vec)

print(vec[::-1])
for column in range(1, m, 2):
    endArr[:,column] = arr[:,column] * vec[::-1]

print(endArr / maxinvec)

sys.stdout.close()
sys.stdin.close()