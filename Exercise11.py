'''
Created on 11 Jul 2017

@author: root
Exercise 11


Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you.
'''

def get_integer(help_text = "Enter an integer: "):
    try:
        return int(input(help_text))
    except Exception as e:
        print(str(e))
    

def is_prime():
    guess = get_integer()
    listRange = list(range(1, guess + 1))

    
    if guess == 1:
        print("Number {} is not prime.".format(guess))
    elif guess == 2:
        print("Number {} is prime.".format(guess))
    else:
        divisorList = [ number for number in listRange if guess % number == 0 ]
        if len(divisorList) == 2:  # Check length of array, if is two is prime 
            print("Number {} is prime.".format(guess))
        else:
            print("Number {} is not prime.".format(guess))

if __name__ == '__main__':
    is_prime()
