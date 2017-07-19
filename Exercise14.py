'''
Created on 19 Jul 2017

@author: root
Exercise 14

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:
    1) Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    2) Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
import random

def getLenA(helpTextA = 'Enter length size of the random list A: '):
    try:
        return int(input(helpTextA))
    except Exception as e:
        print(str(e))
        

def getLenB(helpTextB = 'Enter length size of the random list B: '):
    try:
        return int(input(helpTextB))
    except Exception as e:
        print(str(e))

def getListA():
    return [ random.randrange(1,100) for number in range(getLenA()) ]

def getListB():
    return [ random.randrange(1,100) for number in range(getLenB()) ]

def noDuplicatesLoop():
    listA = getListA()
    listB = getListB()
    print("List A: ")
    print(listA)
    print("List B: ")
    print(listB)
    print("List without duplicates: ")
    return listA + [ number for number in listB if number not in listA ]

def noDuplicatesSet():
    listA = getListA()
    listB = getListB()
    print("List A: ")
    print(listA)
    print("List B: ")
    print(listB)
    print("List without duplicates using set(): ")
    return set(listA + listB)



if __name__ == '__main__':
    print(noDuplicatesLoop())
    print(noDuplicatesSet())



    

