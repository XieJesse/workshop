#Jesse Xie, Qina Liu, Patrick Ging
#SoftDev
#K05: Better Living Through Amalgamation
#2021-09-27

# SUMMARY OF TRIO DISCUSSION
# It's not always necessary to utilize a function to accomplish a task, and simplicity is key
# It's easier to stick to the basics without using outside programs
# Work smarter, not harder
# DISCOVERIES
# Data can be imported from different places so that the code does not be need to be updated
# QUESTIONS
# Is it smarter or just more work to read a file in the context of this assignment?
# COMMENTS
# I thought it was interesting how people retrieved the names from github in different ways

import random

pd1 = [
    "Alejandro Alonso", "Aryaman Goenka", "Angela Zhang", "Christopher Liu", "Deven Maheshwari",
    "Emma Buller", "Ella Krechmer", "Gavin McGinley", "Haotian Gan", "Ivan Lam", "Ishraq Mahid",
    "Ivan Mijacika", "Julia Nelson", "Lucas Lee", "Lucas Tom Wong", "Michelle Lo", "Oscar Wang",
    "Owen Yaggy", "Renggeng Zheng", "Shriya Anand", "Shyne Choi", "Sadid Ethun", "Tomas Acuna", "Theo Fahey",
    "Tina Nguyen", "Tami Takada", "William Chen", "Yusuf Elsharawy", "Zhaoyu Lin"
    ]

print(pd1[random.randint(0, len(pd1)-1)]) #pd1 name generation

pd2 = [
    "Alif Abdullah", "Andrew Juang", "Andy Lin", "Austin Ngan", "Annabel Zhang", "Daniel Sooknanan",
    "Eric Guo", "Eliza Knapp", "Hebe Huang", "Han Zhang", "Yoonah Chang", "Josephine Lee", "Jonathan Wu",
    "Jesse Xie", "Justin Zou", "Kevin Cao", "Liesel Wong", "Michael Borczuk", "Mark Zhu", "Noakai Aronesty",
    "Patrick Ging", "Qina Liu", "Rachel Xiao", "Raymond Yeung", "Sophie Liu", "Shadman Rakib", "Thomas Yu",
    "Wenhao Dong", "Yaying Liang Li", "Yuqing Wu"
    ]

print(pd2[random.randint(0, len(pd2)-1)]) #pd2 name generation
