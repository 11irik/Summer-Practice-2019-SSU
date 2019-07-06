# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s = input()

for char in s:
    if s.count(char) == 2:
        print(char)
        break

