# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

#5.3

n, m = map(int, input('Enter n x m ').split())

a = []

for i in range(n):
    temp = []
    while len(temp) != m:
        print(i + 1, end = ' ')
        print('line')
        temp = list(map(int, input('Enter m elements ').split()))
    a.append(temp)

print(*a, sep = '\n')

mv = a[0][0]
for i in range(n):
    if max(a[i]) > mv:
        mv = max(a[i])

for i in range(n):
    for j in range(m):
        a[i][j] /= mv

print(*a, sep = '\n')