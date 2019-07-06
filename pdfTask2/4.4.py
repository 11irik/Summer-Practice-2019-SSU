# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s1 = input().split()
s2 = input()


for word in s1[::-1]:
    if word in s2:
        print(word)
    break

# hello world, welcome to the city of sins
# my name was given to me for my sins. That's sad