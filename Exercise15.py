'''
Created on 19 Jul 2017

@author: root
Exercise 15

Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:
     My name is Michele
Then I would see the string:
      Michele is name My
shown back to me.
'''


def getString():
    return input("Enter String: ")

def manipulateString():
    stringParsed = getString().split()
    newString = []
    
    for word in stringParsed:
        newString.insert(0, word)
    return " ".join(newString)

if __name__ == '__main__':
    print(manipulateString())
