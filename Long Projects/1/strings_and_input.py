""" File: strings_and_input.py
    Author: Avichal Kaul
    Purpose: Reads some user inputs and processes them in
    various ways, printing lots of information about the string.
"""

def main():
    '''
    This handles all our user input,
    and our printing and processing too.
    '''
    user_input = input('input string: ')
    print(len(user_input)) # length of string
    print(user_input[1]) # second character of string
    print(user_input[:10]) # first 10 characters of string
    print(user_input[-5:]) # last 5 characters of string
    print(user_input.upper()) # uppercase string
    list_1 = ['q','w', 'e', 'r', 't', 'y'] # lists for classifying
    list_2 = ['u', 'i', 'o', 'p'] # the first character of the string
    if user_input[0].isdigit() == True: # into a bunch of categories
        print('DIGIT')
    elif user_input[0].isalpha() == True:
        if user_input[0].lower() in list_1:
            print('QWERTY')
        elif user_input[0] in list_2:
            print('UIOP')
        else:
            print('LETTER')
    else:
        print('OTHER')
    int_1 = input() # reading two numbers and multiplying them
    int_2 = input()
    print(int(int_1)*int(int_2))

main()
