# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

#5.3

n, m = map(int, input().split())

a = []

for i in range(n):
    temp = []
    while len(temp) != m:
        temp = list(map(int, input().split()))
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