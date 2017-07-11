'''
Created on 5 Jul 2017

@author: root
Exercise 7

Let’s say I give you a list saved in a variable: 
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''
import random

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# random list
b = [ random.randrange(1,100) for number in range(random.randrange(1,30)) ]

def isEven():
    print("Even numbers in a: ")
    print([ number for number in a if number % 2 == 0 ])
    print("Even numbers in random list: ")
    print([ number for number in b if number % 2 == 0 ])

if __name__ == '__main__':
    isEven()