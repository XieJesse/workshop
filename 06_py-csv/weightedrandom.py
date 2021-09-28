#Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
#SoftDev
#K06: StI/O: Divine your Destiny!
#2021-09-28

import csv

occupations = {}

with open('occupations.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        occupations[row[0]] = float(row[1])
        
        
print(occupations) 
