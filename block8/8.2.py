import numpy as np
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = map(int, (input().split()))
l, k = map(int, (input().split()))

arr = a = np.random.randint(3, size=n*m).reshape(n,m)
print(arr)

uf, df = np.split(arr, [l,])
ul, ur = np.hsplit(uf, [k,])
dl, dr = np.hsplit(df, [k,])

print('\n',np.sum(ul), np.sum(ur))
print(np.sum(dl), np.sum(dr))
sys.stdout.close()
sys.stdin.close()