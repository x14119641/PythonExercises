'''
Created on 5 Jul 2017

@author: root
Exercise 6

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

def isPalindrome():
    try:
        noun = input("Enter a string to check if it is a palindrome: ")
        if noun.isalpha():
            if noun == noun[::-1]:
                print("{} is a palindrome".format(noun))
            else:
                print("{} ins not a palindrome".format(noun))
        else:
            print("Wrong Input")
            return isPalindrome()
        print("bye")
    except Exception as e:
        print(str(e))

def main():
    isPalindrome()
    
if __name__ == '__main__':
    main()

