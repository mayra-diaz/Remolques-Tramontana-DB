import csv
from random import randint

with open('bd.txt', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='-')
    for i in range(2000000):
      tsv_writer.writerow([str(randint(1970, 1990)), str(randint(1, 12)).rjust(2, '0'), str(randint(1, 28)).rjust(2, '0')])

with open('dates.txt', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='-')
    for i in range(2000000):
      tsv_writer.writerow([str(randint(2005, 2020)), str(randint(1, 12)).rjust(2, '0'), str(randint(1, 28)).rjust(2, '0')])

with open('times.txt', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter=':')
    for i in range(2000000):
      tsv_writer.writerow([str(randint(6, 20)).rjust(2, '0'), str(randint(0, 59)).rjust(2, '0'), str(randint(0, 59)).rjust(2, '0')])
