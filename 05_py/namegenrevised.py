#Jesse Xie
#SoftDev
#Python Revision
#2021-09-26

import random

#function to get a random index from the list
def findRandom(arr):
    length = len(arr)
    index = random.randint(0,length-1) #finds random index from the array, inclusive
    print(arr[index])

pd1 = ["Alejandro Alonso", "Aryaman Goenka", "Angela Zhang", "Christopher Liu", "Deven Maheshwari",
       "Emma Buller", "Ella Krechmer", "Gavin McGinley", "Haotian Gan", "Ivan Lam", "Ishraq Mahid",
       "Ivan Mijacika", "Julia Nelson", "Lucas Lee", "Lucas Tom Wong", "Michelle Lo", "Oscar Wang",
       "Owen Yaggy", "Renggeng Zheng", "Shriya Anand", "Shyne Choi","Sadid Ethun", "Tomas Acuna","Theo Fahey",
       "Tina Nguyen", "Tami Takada", "William Chen", "Yusuf Elsharawy", "Zhaoyu Lin"]

findRandom(pd1) #pd1 name generation

pd2 = ["Alif Abdullah", "Andrew Juang", "Andy Lin", "Austin Ngan", "Annabel Zhang", "Daniel Sooknanan",
       "Eric Guo", "Eliza Knapp", "Hebe Huang", "Han Zhang", "Yoonah Chang", "Josephine Lee", "Jonathan Wu",
       "Jesse Xie", "Justin Zou", "Kevin Cao", "Liesel Wong", "Michael Borczuk", "Mark Zhu", "Noakai Aronesty",
       "Patrick Ging","Qina Liu", "Rachel Xiao", "Raymond Yeung", "Sophie Liu", "Shadman Rakib","Thomas Yu",
       "Wenhao Dong", "Yaying Liang Li", "Yuqing Wu"]

findRandom(pd2) #pd2 name generation
