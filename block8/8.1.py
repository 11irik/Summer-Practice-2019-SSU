import numpy as np

a = np.random.randint(1000, size=12).reshape(6,2)

print(a)                           #1

print('2\n', a[3,1])                #2

print('3\n', a[:,1])                #3

print('4\n', a[::-1,0])

a = np.reshape(a, (3,4))           #5
print('5\n', a)

k = 2
a += k
print('6\n', a)                     #6

print('7\n', a.max(axis=0))         #7

print('8\n', min(a[:,0]))           #8


#-----------------9
n = 50
m = np.random.randint(-10, 10, size = n)
print('9\n', m)

startInd = -1
endInd = -1
for i in range(-1, -n-1, -1):
    if m[i] < 0:
        startInd = i
        break

endInd = startInd
while m[endInd] < 0:
    endInd -= 1

sum = 0
for i in range(startInd, endInd, -1):
    sum += m[i]

print(sum / (endInd - startInd))

#--------------------10

k = np.random.randint(1000, size=64).reshape(8, 8)
print ('10\n', k)

sum = 0
for i in k[0::2, 1::2]:
    sum += np.sum(i)

for i in k[1::2, 0::2]:
    sum += np.sum(i)

print ('\n', sum)

