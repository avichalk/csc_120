""" File: file_of_ints.py
    Author: Avichal Kaul
    Purpose: Takes a file of ints
    and creates a list of ints.
"""


def main():
    '''
    Sorts the contents of a file
    and does stuff with it, then
    prints the results out. If there
    is no file, we print an error.
    '''
    user_in = input()
    try:
        filename = open(user_in, 'r')
    except:
        print('ERROR: File not found')
    else:
        file_list = filename.readlines()
        filelist = []
        for i in sorted(file_list):
            y = []
            x = i.strip('\n')
            k = x.split(' ')
            y.append(int(k[0])) # the numbers were being appended
            y.append(int(k[1])) # as strings, which created a lot
            filelist.append(y) # of problems. This is not the best
        for i in sorted(filelist): # way to deal with it, but it works.
            z = (i[0], i[1])
            print(tuple(z))
main()