""" File:

    Author: Avichal Kaul

    Purpose:

"""


def main():

    ''

    fi_name = input()

    #fi_name = r'proj09-long\pronunc_random1.txt'

    file_dic = file_load(fi_name)

    user_input(file_dic)


def file_load(fi_name):

    ''

    my_file = open(fi_name, 'r')

    file_lines = my_file.readlines()


    file_dic = {}


    for i in file_lines:

        i = [i.strip() for i in i.split(' ') if i] # removes newlines, splits each line, removes blank spaces

        if i[0] in file_dic:

            file_dic[i[0]].append(i[1:])

        else:

            file_dic[i[0]] = []

            file_dic[i[0]].append(i[1:])

         # unless it already exists, in which case it appends the list

        # we might have to change the pronunciation to the key and the word to the item

        # or actually just add a custom check to see how many times a word is duplicated...

        # ask prof

    #print(file_dic)

    my_file.close()

    return file_dic


def user_input(file_dic):

    try:

        inpt = input()

    except:

        return

    #inpt = 'SUMMONED'


    if inpt.strip() == '':

        print('No word given')

        print()

        print()

    elif len(inpt.split(' ')) > 1:

        print('Multiple words entered, please enter only one word at a time.')

        print()

        print()

    else:

        output = rhyme_search(file_dic, inpt.upper())

        print_func(inpt.upper(), sorted(output))

    #print()

    user_input(file_dic)


def print_func(inpt, output):

    print('Rhymes for:', inpt)

    if output != []:

        for i in output:

            print(' ', i)

    else:

        print('  -- none found --')

    print()

# def inpt_handler(file_dic, inpt):

#     for i in file_dic:

#         if file_dic[i] == inpt:

#             to_search = i

#     print(to_search)


def rhyme_search(file_dic, inpt):

    if inpt not in file_dic:

        return []

    # use a set to store what needs to be printed plz

    stress_inpt, phoenome_inpt, subs_inpt = phonemes_and_vowels(file_dic, inpt)

    #print(stressed)

    #print(phoenome)

    output = set()

    # stressed has to be true. phoenome has to be false for the one

    # directly before stressed

    #print(file_dic)

    #print(file_dic)

    for i in file_dic:

        stressed, phoenome, subsequent = phonemes_and_vowels(file_dic, i)

        for j in stress_inpt:

            if stress_inpt == stressed:

                    if phoenome_inpt != phoenome:

                        if len(subs_inpt) == len(subsequent):

                            if subsequent == subs_inpt:

                                output.add(i)

#     for i in sorted(output):

#         print(i)

    #print(sorted(output)) # small error with vansciver and vanskyver. apparently stress does not matter? clarify with prof

    return output


def phonemes_and_vowels(file_dic, inpt):

    #print(file_dic)

    stressed = ''

    phoenome = ''

    subsequent = [] # might have to add a list inside a list for the file_dic

    for j in file_dic[inpt]:

        for i in range(0, len(j)):

            if j[i][-1] == '1': # right here, change it to 0 and then 1 etc.

                if i > 0:

                    stressed = j[i] # need list with primary stress etc in it, then check that

                    phoenome = j[i-1]

                    subsequent = j[i:]

    #print(stressed, phoenome, subsequent)

    return stressed, phoenome, subsequent

#SUMMONED  S AH1 M AH0 N D

#DUDMAN  D AH1 D M AH0 N


# make functino that returns the key to which an item belongs if given item


main()