# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s1 = input().split()
s2 = input().split()
for word in s1[::-1]:
    if word in s2:
        print(word)
        break

# I am a newcomer and that is not bad
# The newcomer was promising