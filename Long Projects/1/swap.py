""" File: swap.py
    Author: Avichal Kaul
    Purpose: Reads an input string from the user and
    swaps the first and second half with each other.
"""

def main():
    '''
    Handles the user input, processes the string,
    then prints the resulting string for the user.
    '''
    string = input('Please give a string to swap: ')
    string = string.strip()
    new_string = '' # we process the string differently
    if len(string)%2==0: # depending on if it is even or odd
        i=int(len(string)/2) # if it is even, we just divide it
        while i<=int(len(string)-1): # in two and swap it
            new_string+=string[i]
            i+=1 # this handles the first half of the string
        i = int(0)
        while i<=int(len(string)/2-1): # this handles the second half
            new_string+=string[i]
            i+=1
        print(new_string)
    else:
        i=int(len(string)/2+1) # if it is odd, we also have to take the exact midpoint and
        while i<=int(len(string)-1): # preserve its position in the string.
            new_string+=string[i]
            i+=1
        new_string+=string[int(len(string)/2)] # this is the midpoint being preserved
        i = int(0)
        while i<=int(len(string)/2-1):
            new_string+=string[i]
            i+=1
        print(new_string)

main()