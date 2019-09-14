import math

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

x, y = map(float, input("x, y: ").split())

if x > 0 or x < -23:
    print("No")
elif y > 0 or y < x:
    print("No")
elif y == x or x == -23 or y == 0:
    print("Bourder")
else:
    print("Yes")
