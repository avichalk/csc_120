""" File: rhymes.py
    Author: Avichal Kaul
    Purpose: Finds perfect rhymes with a dictionary and some files.

    Comments: "Maybe the real rhymes were the friends we made along the way",
    is what I say every single time this program doesn't work. It was off by
    one word, and fixing it took almost three hours. Good god.
"""

def main():
    '''
    Accepts input from user for file name,
    passes through to other functions.
    '''

    fi_name = input()
    file_dic = file_load(fi_name)
    user_input(file_dic)

def file_load(fi_name):
    '''
    Loads the contents of the file into
    a dictionary. Each item is a list.
    Each list has another list inside it.
    Technically, this solution is scaleable
    for as many heteronmyns as you want,
    but please don't test it. Returns the
    file's dictionary.
    '''

    my_file = open(fi_name, 'r')
    file_lines = my_file.readlines()

    file_dic = {}

    for i in file_lines:
        i = [i.strip() for i in i.split(' ') if i] # removes newlines, splits each line, removes blank spaces
        if i[0] in file_dic:
            file_dic[i[0]].append(i[1:]) # if the word already has one pronunciation, it appends
        else:
            file_dic[i[0]] = [] # otherwise it inits a list, *then* appends
            file_dic[i[0]].append(i[1:])

    my_file.close()
    return file_dic

def user_input(file_dic):
    '''
    Handles user input for the word to find,
    until EOF or similar. Prints some responses,
    passes the input through to our other function
    and gets an output, passes output through to
    print function, rinse and repeat. Does not return
    anything.
    '''

    try:
        inpt = input()
    except:
        return

    if inpt.strip() == '':
        print('No word given')
        print()
    elif len(inpt.split(' ')) > 1:
        print('Multiple words entered, please enter only one word at a time.')
        print()
    else:
        output = rhyme_search(file_dic, inpt.upper())
        print_func(inpt.upper(), sorted(output))

    print()
    user_input(file_dic)

def print_func(inpt, output):
    '''
    Prints our output. If there isn't one,
    prints 'none found'. Does not return anything.
    '''

    print('Rhymes for:', inpt)

    if output != []:  # going to have an actual mental breakdown. i realised this was wrong,
        for i in output:  # fixed it in both functions so it was a set, and then THE CODE DIDN'T WORK.
            print(' ', i)  # making it a list again FIXED IT.
    else:
        print('  -- none found --')


def rhyme_search(file_dic, inpt):
    '''
    Searches for rhymes. My initial solution worked perfectly.
    It was beautiful. Then, for just *one* word in *one* testcase,
    I had to scrap it and start over. It loops through all our lists
    and compares them. It returns an output when the words are perfect
    rhymes. FTR perfect rhymes are unrealistic! Regular rhymes FTW.
    '''

    if inpt not in file_dic:
        return []  # this was one of the testcases? for some reason?

    output = set()  # to ensure no duplicates

    for i in file_dic[inpt]:
        stress_inpt, phoenome_inpt, subs_inpt = phonemes_and_vowels(file_dic, i)
        for k in file_dic:
            for j in file_dic[k]:
                stressed, phoenome, subsequent = phonemes_and_vowels(file_dic, j)
                if stress_inpt == stressed:
                    if phoenome_inpt != phoenome:
                        if subsequent == subs_inpt:
                            if k.strip() != '':
                                output.add(k)

    return sorted(output)


def phonemes_and_vowels(file_dic, j):
    '''
    This function cracks our lists open like an egg
    and gets all that soft, gooey information out.
    It originally took in the key, and worked fine.
    But no. Now it takes in lists. It returns the
    stressed phoenome, the phoenome before it, and
    everything after it so it can be checked.
    '''

    stressed = ''
    phoenome = ''
    subsequent = []

    for i in range(0, len(j)):
        if j[i][-1] == '1':
            if i > 0:
                stressed = j[i]
                phoenome = j[i-1]
                subsequent = j[i:]

    return stressed, phoenome, subsequent

main()