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

clearTable = "DROP TABLE IF EXISTS roster"
c.execute((clearTable))
command = "CREATE TABLE IF NOT EXISTS roster (name TEXT, age INTEGER, userid INTEGER) "
c.execute((command))    # run SQL statement

with open('students.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if row[0] != "name":
            info = [row[0], row[1], row[2]]
            addData = "INSERT INTO roster VALUES(?,?,?)"
            c.execute(addData,info)




#==========================================================

db.commit() #save changes
db.close()  #close database
