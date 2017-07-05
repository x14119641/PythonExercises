'''
Created on 5 Jul 2017

@author: root
Exercise 5

Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
    1) Randomly generate two lists to test this
    2) Write this in one line of Python.
'''
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# random list
c = [ random.randrange(1,100) for number in range(random.randrange(1,20)) ]
d = [ random.randrange(1,100) for number in range(random.randrange(1,20)) ]

def noDuplicates():
    # Unordered list
    print("Unordered List: ")
    print(list(set(a+b)))
    
    # Ordered list
    print("Ordered List: ")
    print(sorted(set(a+b)))
    
    # Random lists
    print("Random List without duplicates: ")
    print(list(set(c+d)))
    
def main():
    noDuplicates()
    
if __name__ == '__main__':
    main()
