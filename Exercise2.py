'''
Created on 1 Jul 2017

@author: root
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:
    1) If the number is a multiple of 4, print out a different message.
    2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''


def getInputs():
    try:
        num = int(input("Enter a number to 'check': "))
        check = int(input("Enter the 'check' number: "))
        return num, check
    except Exception as e:
        print(str(e))
    
        
def getOutputs(num, check):
    if num % 4 == 0:
        print("The number {} is multiple of 4".format(num))
        
    elif num % 2 != 0:
        print("The number {} is odd.".format(num))
    else:
        print("The number {} is even.".format(num))
        
    if (num % check) == 0:
        print("The number {} 'to check' is evenly divided by {}".format(num, check))
    else:
        print("The number {} 'to check' is not evenly divedid by {}".format(num, check))

def main():
    inputs = list(getInputs())

    getOutputs(inputs[0], inputs[1])

if __name__ == '__main__':
    main()        