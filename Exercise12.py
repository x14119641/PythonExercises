'''
Created on 18 Jul 2017

@author: root
Exercise 12

Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''
import random

def randomList():
    return [ random.randrange(1,100) for number in range(random.randrange(1,30)) ]


def getEdge():
    list = randomList()
    print(list)
    print([list[0], list[-1]])


if __name__ == '__main__':
    getEdge()