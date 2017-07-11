'''
Created on 11 Jul 2017

@author: root
Exercise 10

Similar exercise of Exercise 5 "Duplicates"
'''
import random
from Crypto.Random.random import randint

# Random lists
a = random.sample(range(100), randint(1,15))
b = random.sample(range(100), randint(1,10))

def noDuplicates():
    print("Random list a: ")
    print(a)
    print("Random list b: ")
    print(b)
    # Random lists
    print("Random List without duplicates: ")
    print(sorted(list(set(a+b))))

if __name__ == '__main__':
    noDuplicates()
    