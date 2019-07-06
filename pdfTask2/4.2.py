# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s = input()
a, b = input().split()


print(s.count(a) * a)
print(s.count(b) * b)
