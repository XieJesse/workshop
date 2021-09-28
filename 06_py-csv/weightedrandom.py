#Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
#SoftDev
#K06: StI/O: Divine your Destiny!
#2021-09-28

#SUMMARY
# We first had to read the file and put the data into a dictionary. After that,
# we created a method that generated a random value within the total of the
# data. We subtracted the perecentages from each job class from our random value
# until the total fell into the range of the values of the key, in which the key would be returned.

import csv
import random

occupations = {}

with open('occupations.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if (row[0] != "Job Class"):
            occupations[row[0]] = float(row[1]) # add each line to the dictionary

def select_occupation(occupations_dict):
    rand_total = random.uniform(0.0,occupations_dict["Total"]) # generate a random number
    del(occupations_dict["Total"]) # delete total from dictionary just in case
    for key, value in occupations_dict.items(): # for each key and value in the items of the dictionary
        rand_total -= value # subtract from the random total generated
        if (rand_total <= 0): 
            print(key) # return the key if the total falls into the range
            break
        
select_occupation(occupations)
    


