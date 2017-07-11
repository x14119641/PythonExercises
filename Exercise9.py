'''
Created on 11 Jul 2017

@author: root
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:
    1) Keep the game going until the user types “exit”
    2) Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random


points = []

def game():
    number = random.randint(1,9)
    while True:
        try:
            guess = int(input("What is the number to guess?: "))
            if guess not in range(0,10):
                print("Wrong number, starting again...")
                return game()
            if guess > number:
                print("Number too high")
            
            elif guess < number:
                print("Number too low")
                
            else:
                print("Correct number")
                points.append(1)
                repeat = input("Enter exit to end the application: ")
                if repeat.lower() == "exit":
                    False
                    print("You guess the number {} times.".format(sum(points)))
                    return
        
        except Exception as e:
            print(str(e))
      

if __name__ == '__main__':
    game()
    
    
    
    
    