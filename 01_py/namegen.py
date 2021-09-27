#Jesse Xie
#SoftDev
#2021-09-21

import random

#function to get a random index from the list
def findRandom(arr):
    length = len(arr)
    index = random.randint(0,length-1) #finds random index from the array, inclusive
    print(arr[index])

pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Ishraq Mahid", "Kevin Cao", "Ivan Lam", "Michelle Lo"]
findRandom(pd1) #uses function to generate random name from the list

pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Patrick Ging", "Yaying Liang", "Raymond Yeung"]
findRandom(pd2)
