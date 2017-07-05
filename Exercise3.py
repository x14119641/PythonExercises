'''
Created on 2 Jul 2017

@author: root
Exercise 3

Take a list, say for example this one: 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
    1) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    2) Write this in one line of Python.
    3) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def lessThan5():
    print([ number for number in a if number < 5 ])

def lessThanX():
    try:
        check = int(input("Enter a number: "))
        print("The following list contains all the numbers that are less than {} in the 'a' list".format(check))
        print( [number for number in a if number < check] )
    except Exception as e:
        print(str(e))
    
    
    
def main():
    lessThan5()
    lessThanX()
    
if __name__ == '__main__':
    main()
            