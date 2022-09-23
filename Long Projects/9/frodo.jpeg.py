""" File:
    Author: Avichal Kaul
    Purpose:
"""

def main():
    ''
    #print('here')
    fi_name = input()
    #fi_name = r'proj09-long\PronunciationDictionary.txt'
    file_dic = file_load(fi_name)
    #print('here')
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
    #inpt = 'however'

    if inpt.strip() == '':
        print('No word given')
        print()
    elif len(inpt.split(' ')) > 1:
        print('Multiple words entered, please enter only one word at a time.')
        print()
    else:
        output = rhyme_search(file_dic, inpt.upper())
        print_func(inpt.upper(), sorted(output))
        #print()
    print()
    user_input(file_dic)

def print_func(inpt, output):
    print('Rhymes for:', inpt)
    if output != []:
        for i in output:
            print(' ', i)
    else:
        print('  -- none found --')


def rhyme_search(file_dic, inpt):
    if inpt not in file_dic:
        return []
    # use a set to store what needs to be printed plz
    #print(stressed)
    #print(phoenome)
    output = set()
    # stressed has to be true. phoenome has to be false for the one
    # directly before stressed
    #print(file_dic)
    #print(file_dic)
    for i in file_dic[inpt]:
        stress_inpt, phoenome_inpt, subs_inpt = phonemes_and_vowels(file_dic, i)
        for k in file_dic:
            for j in file_dic[k]:
                stressed, phoenome, subsequent = phonemes_and_vowels(file_dic, j)
                if stress_inpt == stressed:
                    if phoenome_inpt != phoenome:
                        if len(subs_inpt) == len(subsequent):
                            if subsequent == subs_inpt:
                                if k.strip() != '':
                                    output.add(k)
    #print(sorted(output))
    return sorted(output)


def phonemes_and_vowels(file_dic, j): # redo this so it's not the inpt we're feeding in, it's the list.
    #print(j)
    stressed = ''
    phoenome = ''
    subsequent = [] # might have to add a list inside a list for the file_dic
    for i in range(0, len(j)):
        if j[i][-1] == '1':
            #print(k[i])
            if i > 0:
                stressed = j[i] # need list with primary stress etc in it, then check that
                phoenome = j[i-1]
                subsequent = j[i:]
    #print(stressed, phoenome, subsequent)
    return stressed, phoenome, subsequent

#SUMMONED  S AH1 M AH0 N D
#DUDMAN  D AH1 D M AH0 N
#LEVER  L EH1 V ER0
#LEVER  L IY1 V ER0

# make functino that returns the key to which an item belongs if given item

main()