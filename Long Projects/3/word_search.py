""" File:
    Author: Avichal Kaul
    Purpose: I hurt my back really badly this weekend and fell
    behind on my work. That's my excuse.
"""

def main():
    '''
    '''
    words_list, grid_list = open_file()
    words_list = reverse_words_list(words_list)
    find_words(words_list, grid_list)


def open_file():
    '''
    '''
    print('Please give the puzzle filename:')
    #fi_name = input()
    fi_name = 'proj03-long/test-word_search-puzzle10.in'
    try:
        file = open(fi_name, 'r')
    except:
        print("Sorry, the file doesn't exist or cannot be opened.")
        exit()
    file_list = file.readlines()
    grid_list = []
    words_list = []
    x=0
    for i in file_list:
        i = i.strip()
        if x==0:
            if i == '':
                x+=1
            else:
                grid_list.append(i)
        if x==1:
            if i!='':
                words_list.append(i)
    #print(words_list, grid_list)
    return words_list, grid_list

def reverse_words_list(words_list):
    '''
    '''
    rev_words_list = []
    for i in words_list:
        rev_i = ''
        x = len(i) - 1
        while x>=0:
            rev_i += i[x]
            x-=1
        rev_words_list.append(rev_i)
    for j in rev_words_list:
        words_list.append(j)
    return words_list

def find_words(words_list, grid_list):
    '''
    '''
    out = []
    x = find_em_sideways(words_list, grid_list)
    for tup in x:
        print_em_sideways(words_list, new_grid_list, tup[1], tup[0])
    y, str_list = find_em_upwards(words_list, grid_list)
    for tup in y:
        print_em_upwards(str_list, words_list, tup[0], tup[1])
    ltr, rtl = find_em_diagonally(words_list, grid_list)
    for tup in ltr:
        str_list_right_to_left, str_list_left_to_right = diag_str_lists(grid_list)
        print_em_left_to_right(str_list_left_to_right, tup[0], tup[1], grid_list)


def find_em_sideways(words_list, grid_list):
    '''
    '''
    new_grid_list = []
    for i in grid_list:
        new_grid_list.append(i)
    i = 0
    words = []
    while i < len(words_list):
        j = 0
        while j < len(new_grid_list):
            if words_list[i] in new_grid_list[j]:
                #print_em_sideways(words_list, new_grid_list, j, i)
                words.append((i, j))
            j+=1
        i+=1
    return words

def find_em_upwards(words_list, grid_list):
    '''
    '''
    i=0
    str_list = []
    while i<len(grid_list[0]):
        j=0
        str_i = ''
        while j<len(grid_list):
            str_i+=grid_list[j][i]
            j+=1
        str_list.append(str_i)
        i+=1
    words = []
    h = 0
    while h < len(str_list):
        k = 0
        while k < len(words_list):
            if words_list[k] in str_list[h]:
                #print_em_upwards(str_list, words_list, k, h)
                words.append((k, h))
            k+=1
        h += 1
    return words, str_list

def find_em_diagonally(words_list, grid_list):
    '''
    '''
    ltr = []
    rtl = []
    str_list_right_to_left, str_list_left_to_right = diag_str_lists(grid_list)
    for i in words_list:
        j = 0
        while j < len(str_list_left_to_right):
            if i in str_list_left_to_right[j]:
                #print_em_left_to_right(str_list_left_to_right, i, j, grid_list)
                ltr.append((i, j))
            if i in str_list_right_to_left:
                print('oof')
                rtl.append((i, j))
            j+=1
    return ltr, rtl

def print_em_upwards(str_list, words_list, k, h):
    '''
    '''
    new_string_list = []
    for i in str_list:
        new_string_list.append(i)
    new_string_list[h] = new_string_list[h].replace(words_list[k], '*'*len(words_list[k]))
    new_list = []
    for o in new_string_list:
        str_var = ''
        for m in o:
            if m != '*':
                str_var += '.'
            else:
                str_var += '*'
        new_list.append(str_var)

    new_list[h] = (new_list[h].replace('*'*(len(words_list[k])), words_list[k]))
    new_str_list = []

    k = 0
    while k<len(new_list[0]):
        j=0
        str_i = ''
        while j<len(new_list):
            str_i+=new_list[j][k]
            j+=1
        new_str_list.append(str_i)
        k+=1
    for i in new_str_list:
        print(i)


def print_em_sideways(words_list, grid_list, j, i):
    grid_list[j] = (grid_list[j].replace(words_list[i], '*'*len(words_list[i])))
    new_grid_list = []
    for k in grid_list:
        str_var = ''
        for m in k:
            if m != '*':
                str_var += '.'
            else:
                str_var += '*'
        new_grid_list.append(str_var)
    new_grid_list[j] = (new_grid_list[j].replace('*'*len(words_list[i]), words_list[i]))
    for i in new_grid_list:
        print(i)


def print_em_left_to_right(str_list_left_to_right, i, j, grid_list):
    new_str_list = []
    for o in str_list_left_to_right:
        new_str_list.append(o)
    new_str_list[j] = new_str_list[j].replace(i, '*'*len(i))
    a = 0
    rev_grid_list = [''] * len(grid_list)
    i = 0
    while i < len(grid_list):
        m = len(grid_list[0])-1
        while m >= 0:
            rev_grid_list[i] += grid_list[i][m]
            m-=1
        i += 1
    a = len(rev_grid_list)-1
    str_var = ''
    a_val = []
    b_val = []
    while a >= 0:
        b = 0
        while b < len(rev_grid_list[0]):
            if a + b == j:
                str_var += rev_grid_list[a][b]
                a_val.append(len(rev_grid_list)-a)
                b_val.append(b)
            b+=1
        a-=1
    new_list = []
    i = 0
    while i < len(grid_list):
        str_var = ''
        m = 0
        x=0
        while x < len(a_val):
            while m < len(grid_list[0]):
                    if (i, m) != (a_val[x], b_val[x]):
                        str_var += '.'
                    else:
                        str_var += grid_list[i][m]
                    m+=1
            new_list.append(str_var)
            x+=1
        i+=1
    for i in new_list:
        print(i)

def diag_str_lists(grid_list):
    '''
    '''
    a = 0
    str_list_right_to_left = ['']*(len(grid_list)+len(grid_list[0])-1)
    while a < len(grid_list):
        b = 0
        while b < len(grid_list[0]):
            c = 0
            while c < len(grid_list)+len(grid_list[0]):
                if a+b == c:
                    str_list_right_to_left[c] += grid_list[a][b]
                c+=1
            b+=1
        a+=1
    str_list_left_to_right = ['']*(len(grid_list)+len(grid_list[0])-1)
    rev_grid_list = [''] * len(grid_list)
    i = 0
    while i < len(grid_list):
        j = len(grid_list[0])-1
        while j >= 0:
            rev_grid_list[i] += grid_list[i][j]
            j-=1
        i += 1
    a = len(rev_grid_list)-1
    while a >= 0:
        b = 0
        while b < len(rev_grid_list[0]):
            c = len(rev_grid_list)+len(rev_grid_list[0])-2
            while c >= 0:
                if a+b == c:
                    str_list_left_to_right[c] += rev_grid_list[a][b]
                c-=1
            b+=1
        a-=1
    return str_list_right_to_left, str_list_left_to_right


main()