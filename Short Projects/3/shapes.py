""" File: shapes.py
    Author: Avichal Kaul
    Purpose: some linked arrays, some
    recursive ones.
"""

def shape_alpha():
    '''
    Returns a list filled with lists.
    '''
    list_1 = [10, "abc", "jkl", 40]
    list_2 = [1.1, -17]
    list_3 = [123, 456]
    list_4 = [list_2, list_3]
    main_list = [list_1, list_4]
    return main_list

def shape_bravo():
    '''
    Returns a list filled with lists.
    '''
    list_1 = ["bogus", "righteous"]
    list_2 = ['whoa', 'excellent']
    list_3 = [list_2, list_1]
    list_4 = [list_1, "rufus"]
    main_list = [list_3, list_4]
    return main_list

def shape_charlie(arg1):
    '''
    Accepts one parameter.
    Returns a list filled with lists.
    '''
    list1 = [None, arg1]
    list2 = [list1[0], arg1]
    list3 = [list2[0], arg1]
    list4 = [list3[0], arg1]
    return list4

def shape_delta(arg1, arg2):
    '''
    Accepts two parameters.
    Returns a list filled with lists.
    '''
    list_1 = [arg1, arg2]
    ref_1 = [30]
    list_2 = [arg1, arg2, list_1, ref_1]
    ref_2 = [20]
    list_3 = [arg1, list_2, ref_2, arg2]
    ref_3 = [10]
    list_4 = [arg1, arg2, list_3, ref_3]
    return list_4

def shape_echo(arg1, arg2, arg3):
    '''
    Accepts 3 parameters.
    Returns a list filled with lists.
    '''
    list_1 = [None, arg3]
    list_2 = [list_1, arg2]
    list_3 = [list_2, arg1]
    list_1[0] = list_3
    return list_3
