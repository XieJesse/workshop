import csv
import random

# format: {
#   [job]: ([percentage], [link])
# }
# The key is the job class, the value is a tuple of the percentage and link

data = {}

with open("data/occupations.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row[0] != "Job Class" and row[0] != "Total":
            data[row[0]] = (float(row[1]), row[2])

jobs = list(data.keys())
weights = []
for value in data.values():
    weights.append(value[0])

def random_occupation():
    return random.choices(jobs, weights=weights)[0]
