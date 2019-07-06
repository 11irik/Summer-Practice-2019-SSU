import numpy as np
import random
import sys
import time
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def listlinesmax(l):
    maxs = []
    for line in l:
        maxs.append(max(line))
    return maxs

n = 1000
m = 1000

lst = []
for i in range(n):
    tmp = []
    for i in range(m):
        tmp.append(random.randrange(1, 101, 1))
    lst.append(tmp)


numpyArr = np.asarray(lst)

t1 = time.time()
for i in range(10):
    listlinesmax(lst)
t2 = time.time()
print((t2-t1))

t1 = time.time()
for i in range(10):
    np.max(numpyArr, axis=1)
t2 = time.time()
print((t2-t1))

sys.stdout.close()
sys.stdin.close()