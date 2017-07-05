'''
Created on 30 Jun 2017

@author: root

Exercise 1
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
    1) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    2) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
import datetime

def getInputs():
    try:
        name = input("Enter your Name: ")
        age = int(input("Enter your Age: "))
        repetitions = int(input("How many times to repeat this message: "))
        return name, age, repetitions
    except Exception as e:
        print(str(e))
    

def whenHundredYears(name, age, repetitions):
    
    i=0
    
    if age > 100:
        
        while i < repetitions:
            i += 1  
            print("{} You are already 100 years old".format(name))
    else:
        calculsYear = (100 - age) + datetime.datetime.now().year
        while i < repetitions:
            i += 1
            print("{} You Will be a 100 years on {}".format(name, calculsYear))
    print("...bye")
        

def main():
    inputs = list(getInputs())
    whenHundredYears(inputs[0], inputs[1], inputs[2])
    
if __name__ == '__main__' :
    main()










































