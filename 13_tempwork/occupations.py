import csv
import random

data = {}

with open("data/occupations.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row[0] != "Job Class" and row[0] != "Total":
            data[row[0]] = float(row[1])

jobs = list(data.keys())
weights = list(data.values())

def random_occupation():
    return random.choices(jobs, weights=weights)[0]
