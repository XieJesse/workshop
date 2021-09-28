import csv

occupations = {}

with open('occupations.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        occupations[row[0]] = row[1]
        
print(occupations) 
