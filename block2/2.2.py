import math

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s = input()

if int(s[0]) > int(s[1]):
    print('First')
elif int(s[0]) < int(s[1]):
    print("Second")
else:
    print('Equil')
