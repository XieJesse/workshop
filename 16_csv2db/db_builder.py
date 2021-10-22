#Team threeCoffeePeanuts: Jesse Xie, Yaying Liang Li, Ryan Wang
#SoftDev
#K16 -- All About Database
#2021-10-20

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

#roster table
clearTable = "DROP TABLE IF EXISTS roster" # clear if the tables exists
c.execute((clearTable))
command1 = "CREATE TABLE IF NOT EXISTS roster (name TEXT, age INTEGER, id INTEGER) " # create table if it does not exist with parameters
c.execute((command1))    # run SQL statement

with open('students.csv') as csv_file: # read students csv file
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if row[0] != "name":
            info = [row[0], row[1], row[2]] # add data from csv file to list
            addData = "INSERT INTO roster VALUES(?,?,?)" # accept parameters in values
            c.execute(addData,info) # add parameters to addData command

#classes table
clearTable = "DROP TABLE IF EXISTS classes" # clear if the tables exists
c.execute((clearTable))
command2 = "CREATE TABLE IF NOT EXISTS classes (name TEXT, mark INTEGER, id INTEGER) " # create table if it does not exist with parameters
c.execute((command2))    # run SQL statement

with open('courses.csv') as csv_file: # read classes csv file
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if row[0] != "code":
            info = [row[0], row[1], row[2]] # add data from csv file to list
            addData = "INSERT INTO classes VALUES(?,?,?)" # accept parameters in values
            c.execute(addData,info) # add parameters to addData command


#==========================================================

db.commit() #save changes
db.close()  #close database
