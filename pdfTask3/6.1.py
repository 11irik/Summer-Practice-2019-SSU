import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def sequence(n):
    list = [2, 1]
    if n > 2:
        i = 2
        while i < n:
            list.append(2/3 * list[i - 2] - 1/3 * list[i - 1]**2)
            i += 1
        return list
    elif n == 2:
        return list
    else:
        return list[1:]


n = int(input())
print(*sequence(n))
