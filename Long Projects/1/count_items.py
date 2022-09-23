""" File: count_items.py
    Author: Avichal Kaul
    Purpose: Counts and sorts various items
    from a file provided by the user.
"""

import os


def main():
    '''
    Handles the user inputs, and passes everything through
    to other functions. Also has some code the instructors
    wanted us to put in.
    '''
    # chdir to the same directory as where this script is ... so
    # that open() will open the file we expect.
    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)
    user_input = input('File to scan: ')
    file_list = file_processing(user_input)
    word_dic = calculating(file_list)
    unsorted_array = sort_tuples(word_dic)
    printing_stuff(file_list, word_dic, unsorted_array)


def file_processing(user_input):
    '''
    Removes junk data from our input file,
    puts the rest into a list, and returns that list to main
    '''
    filename = open(user_input.strip())
    filelist = filename.readlines()
    file_list = []
    filelist1 = []
    for i in filelist:
        i_new = i.replace('\t', '') # these \ts weren't easy to remove
        filelist1.append(i_new) # as you can probably tell
    for i in filelist1: # removes some unessecary stuff from our data
        i = i.strip()
        if i != '':
            if i[0] != '#':
                file_list.append(i)
    return file_list


def calculating(file_list):
    '''
    Splits the data in each line
    into a word and an integer, and puts
    them into a dictionary as key and value.
    Returns that dictionary to main.
    '''
    word_dic = {}
    for i in file_list:
        char = ''
        num = ''
        for j in i:
            if j != ' ': # sometimes there are spaces, sometimes there aren't
                if j == '-':
                    num+=j # accounting for -ve numbers
                elif j.isnumeric() == False:
                    char+=j # if the thing isn't numeric,
                else: # we consider it a part of the word
                    num+=j
        if char in word_dic:
            word_dic[char]+=int(num) # if the key already exists, we add
        else:
            word_dic[char] = int(num) # otherwise, we initialize
    return word_dic


def sort_tuples(word_dic):
    '''
    Sorts the dictionary into tuples
    and returns them to main
    '''
    unsorted_array = []
    for i in sorted(word_dic): # does some amount of sorting?
        unsorted_array.append((word_dic[i], i))
    return unsorted_array


def printing_stuff(file_list, word_dic, unsorted_array):
    '''
    Prints all the stuff, also does a lot of the sorting.
    '''
    print('STEP 1: THE ORIGINAL DICTIONARY')
    for key in sorted(word_dic):
        print('Key:', key, 'Value:', word_dic[key])
    print('\nSTEP 2: A LIST OF VALUE->KEY TUPLES')
    print(unsorted_array)
    print('\nSTEP 3: AFTER SORTING')
    print(sorted(unsorted_array))
    print('\nSTEP 4: THE ACTUAL OUTPUT')
    for i in sorted(unsorted_array):
        print(i[1], i[0])


main()