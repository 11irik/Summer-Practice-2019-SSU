# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def removeMultiples(ls, k):
    i = 0
    while i < len(ls):
        if ls[i] % k == 0:
            ls.pop(i)
        else:
            i += 1

l = list(map(int, input().split()))
removeMultiples(l, min(l))
print(*l)