# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def Calculation(a, b):
    return ( (a + b)**3 - (a**3 + 3 * a**2 * b) ) / ( 3 * a * b**2 + b**3 + 3 * a**2 * b )

a, b = map(float, input().split())

print(Calculation(a, b))