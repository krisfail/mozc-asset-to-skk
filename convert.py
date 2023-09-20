import csv

with open('input.tsv', encoding='utf-8') as input:
        dict = [row for row in csv.reader(input, delimiter='\t')]
print(dict)
for ro in dict:
    ro.pop()
print(dict)
