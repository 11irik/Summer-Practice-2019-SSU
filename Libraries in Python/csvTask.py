import sys
import csv

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

berezki_sum = 0
berezki_count = 0
petrol = 0

with open('task19.csv', newline='') as csvfile:
    file_ = csv.reader(csvfile, dialect=csv.excel, delimiter=';')
    for row in file_:
        if '1 октября' <= row[0] <= '3 октября':
            petrol += int(row[4])
        if row[1] == 'Березки':
            berezki_count += 1
            berezki_sum += int(row[5])

    print('First answer:', petrol)
    print('Second anwer:', berezki_sum / berezki_count)


