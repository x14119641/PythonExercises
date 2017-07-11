'''
Created on 5 Jul 2017

@author: root
Exercise 8

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:
    * Rock beats scissors
    * Scissors beats paper
    * Paper beats rock
'''
import random

choices_list = ['rock', 'scissors', 'paper']

def game():
    user_choice = input("Rock, Scissors and Paper: ") 
    machine_choice = random.choice(choices_list)
 
    if user_choice.lower() == 'rock' and machine_choice == 'scissors' or user_choice.lower() == 'scissors' and machine_choice == 'paper' or user_choice.lower() == 'paper' and machine_choice == 'rock':
        print("Player selected {} and machine selected {}"
                  .format(user_choice.lower(),machine_choice))
        print("Player wins")
        return new_game()
    
    elif user_choice.lower() == machine_choice:
        print("Player selected {} and machine selected {}"
                  .format(user_choice.lower(),machine_choice))
        print("Draw") 
        return game()  
            
    elif user_choice.lower() not in machine_choice:
        print("Wrong selection.")
        return game()
            
    else:
        print("Player selected {} and machine selected {}"
                  .format(user_choice.lower(),machine_choice))
        print("Player loses")
        return new_game()
        

def new_game():
    repeat = input("Would you like to play again?: (Y/N) ")
    if repeat.lower() in ['y', 'yes']:
        return game()
    elif repeat.lower() in ['n', 'no']:
        print("Exit")
    else:
        print("Wrong selection")
        return new_game()
         
        
if __name__ == '__main__':
    game()