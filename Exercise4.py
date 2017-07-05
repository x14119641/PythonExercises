'''
Created on 2 Jul 2017

@author: root
Exercise 4

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def divisorsList():
    try:
        check = int(input("Enter a number: "))
        listRange = list(range(1, check + 1))
        print([ number for number in listRange if check % number == 0 ])
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    divisorsList()