import sys
import random
import string

#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')


def isoddsumgreater(st):
    sumOdd = 0
    sumEven = 0

    for i in st[::2]:
        sumOdd += int(i)

    for i in st[1::2]:
        sumEven += int(i)

    if sumOdd > sumEven:
        return True
    else:
        return False


def isidenticalconsonants(st):
    vowels = 'aeiou'
    for i in range(len(st)-1):
        if not (st[i] in vowels or st[i+1] in vowels):
            return True

    return False


def isnumberofevengreater(st):
    odds = []
    evens = []

    for i in st:
        if i.isdigit():
            if int(i) % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

    if len(evens) > len(odds):
        return True
    else:
        return False


def isgreatletter(st):
    for i in st:
        if i in string.ascii_uppercase:
            return True

    return False

def idgenerator():
    s = ''
    k = s.join(random.sample(string.digits, 5))
    while not isoddsumgreater(k):
        k = s.join(random.sample(string.digits, 5))

    return k


def logingenerator():
    s = ''
    k = s.join(random.sample(string.ascii_lowercase, 6))
    while isidenticalconsonants(k):
        k = s.join(random.sample(string.ascii_lowercase, 6))
    return k


def passwordgenerator():
    s = ''
    k = s.join(random.sample(string.ascii_letters + string.digits, 10))
    while not(isnumberofevengreater(k) and isgreatletter(k)):  #or isgreatletter(k)  isnumberofevengreater(k)
        k = s.join(random.sample(string.ascii_letters + string.digits, 10))

    return k


def ispassword(base, st):
    for i in base:
        if i[2] == st:
            return True

    return False


def islogin(base, st):
    for i in base:
        if i[1] == st:
            return True

    return False


def isid(base, st):
    for i in base:
        if i[0] == st:
            return True

    return False

n = 15
base = []
for i in range(n):
    id = idgenerator()
    login = logingenerator()
    password = passwordgenerator()

    while isid(base, id):
        id = idgenerator()

    while islogin(base, login):
        login = logingenerator()

    while ispassword(base, password):
        password = passwordgenerator()

    base.append(tuple((id, login, password)))


print(*base, sep='\n')








