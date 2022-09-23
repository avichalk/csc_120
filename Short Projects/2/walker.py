""" File: walker.py
    Author: Avichal Kaul
    Purpose: Tiny program to change
    x,y coordinates depending on user input.
"""

def main():
    '''
    Handles user input and runs an infinite
    loop that only breaks once there are no
    more user inputs left. Also changes some
    variables based on user input.
    '''
    x=0
    y=0
    while True:
        try:
            user_in = input()
        except:
            break
        if user_in == 'n':
            y+=1
        if user_in == 'e':
            x+=1
        if user_in == 's':
            y-=1
        if user_in == 'w':
            x-=1
        z = (x,y)
        print(z)

main()