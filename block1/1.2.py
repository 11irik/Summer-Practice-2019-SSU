import math

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def calculateArea(a, b, angle):
    return 0.5 * a * b * math.sin(angle)


a, b, angle = map(float, input('a, b, angle: ').split())

answer = input('Is angle in radians? y/n: ')


if answer == 'n':
    angle = angle * 180 / math.pi

print(calculateArea(a, b, angle))

