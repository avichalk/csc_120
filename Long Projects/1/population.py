""" File: population.py
    Author: Avichal Kaul
    Purpose: Processes a file full of data, performs
    a calculation on it, and then prints the results.
"""
import os

def main():
    '''
    Handles the user input, acts as pass through to other functions,
    and has a bit of code the instructors told us to put here.
    '''
    # chdir to the same directory as where this script is ... so
    # that open() will open the file we expect.
    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)
    user_input = input('file: ')
    file_list = file_processing(user_input)
    city_list, pop_list = calculating(file_list)
    output(city_list, pop_list)

def file_processing(user_input):
    '''
    Processes the file name and the data in the file,
    removing certain unnessecary bits, puts them all
    into a list, then returns that list to main.
    '''
    filename = open(user_input.strip())
    filelist = filename.readlines()
    file_list = []
    for i in filelist:
        i = i.strip()
        if i != '':
            if i[0] != '#':
                file_list.append(i)
    return file_list

def calculating(file_list):
    '''
    Takes the data from file_list, and
    splits it into two different lists-
    city_list and pop_list, corresponding
    to each city's name and population.
    It returns these lists to main.
    '''
    city_list = []
    pop_list = []
    for i in file_list:
        city_name = ''
        population = ''
        for j in i:
            if j.isnumeric() == True: # it it is a number,
                population+=j # we add it to the population figure
            else: # note: population is a string. it will be made
                city_name+=j # into an int later.
        city_list.append(city_name.strip())
        pop_list.append(population)
    return city_list, pop_list

def output(city_list, pop_list):
    '''
    Handles the calculations for total number of
    states/territories and total population. Also
    handles all the printing.
    '''
    i = 0
    pop_tot = 0
    while i<len(city_list):
        print('State/Territory:', city_list[i])
        print('Population:     ', pop_list[i])
        pop_tot+=int(pop_list[i])
        print('')
        i+=1
    print('# of States/Territories:', len(city_list))
    print('Total Population:       ', pop_tot)

main()