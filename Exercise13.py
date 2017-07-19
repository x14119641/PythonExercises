'''
Created on 19 Jul 2017

@author: root
Exercise 13

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def getNumber(helpText = 'Enter number of repetitions in the Fibonacci Sequence: '):
    '''Get user number input
    
        Returns: input number'''
    try:
        return int(input(helpText))
    except Exception as e:
        print(str(e))

def fibonnaci():
    '''Fibonnaci secuence
        
        Returns: Fibonacci sequence according user input.
        
        args: trigguers getNumber() function to get a number'''
    list = [1,1]
    for number in range(getNumber()):
        list.append(list[-1] + list[-2])
    print(list[:-2])
    
if __name__ == '__main__':
    fibonnaci()
        
        