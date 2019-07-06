import sys
sys.stdout = open('output.txt', 'w')

students = []
with open('input.txt', 'r') as in_file:
    for line in in_file:
        students.append(line.split())

    #-min(x[3], x[4], x[5], x[6], x[7])

    for student in sorted(students, key = lambda x: [x[2], -int(min(x[-5:]))]):
        print(*student)
