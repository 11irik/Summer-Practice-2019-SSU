import math

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s = input()
d = []
for i in range(len(s)):
    d.append(int(s[i]))

print(d[1] - d[0] > 0 and d[2] - d[1] > 0 or d[1] - d[0] < 0 and d[2] - d[1] < 0)