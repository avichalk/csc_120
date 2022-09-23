""" File: cb_solver.py
    Author: Avichal Kaul
    Purpose: Solves a board of peg solitaire.
    I wonder why it's called peg solitaire.
"""

def print_board(enc):
    '''
    Takes a string as an input and prints it in board format.
    Does not return anything.
    '''
    strings = [f'{enc[0]}', \
    f'{enc[1]} {enc[2]}', \
    f'{enc[3]} {enc[4]} {enc[5]}', \
    f'{enc[6]} {enc[7]} {enc[8]} {enc[9]}',\
    f'{enc[10]} {enc[11]} {enc[12]} {enc[13]} {enc[14]}']

    for i in range(5):
        print(' '*(4-i) + strings[i])

def get_all_conceivable_moves():
    '''
    Returns a list of all possible moves on our board.
    Does not take any parameters.
    '''
    # first straight down all sides, then inside diags, then straight along inside
    moves = ((0, 2, 5), (2, 5, 9), (5, 9, 14), (0, 1, 3), \
    (1, 3, 6), (3, 6, 10), (10, 11, 12), (11, 12, 13), (12, 13, 14), \
    (2, 4, 7), (5, 8, 12), (4, 7, 11), (1, 4, 8), (4, 8, 13), \
    (3, 7, 12), (3, 4, 5), (6, 7, 8), (7, 8, 9))
    moves = set(moves)
    rev_moves = set()
    for i in moves:
        x = (i[2], i[1], i[0])
        rev_moves.add(tuple(x))
    final = moves.union(rev_moves)
    return final

def get_moves(enc):
    '''
    Gets all moves that are possible at any given
    encoding. Takes a str as an input, returns a set
    of tuples.
    '''
    totset = get_all_conceivable_moves()
    indices = get_indices(enc)
    moves = set()
    for move in totset:
        if move[0] in indices:
            if move[1] in indices:
                if move[2] not in indices:
                    moves.add(move)
    return moves

def get_indices(enc):
    '''
    Takes an encoding and returns the indexes
    populated by 1s (pegs).
    '''
    ones = set()
    i = 0
    while i < len(enc):
        if enc[i] == '1':
            ones.add(i)
        i += 1
    return ones

def cb_one(enc):
    '''
    Recursive function that takes an
    encoding and returns a solution.
    '''
    if len(get_indices(enc)) == 1:
        return []
    moves = get_moves(enc)
    for move in moves:
        new_enc = list(enc)
        new_enc[move[0]] = '0'
        new_enc[move[1]] = '0'
        new_enc[move[2]] = '1'
        x = cb_one(new_enc)
        if x is not None:
            return [move] + x

def _cb_all(enc):
    '''
    Recursive function that takes an
    encoding and returns all possible solutions.
    '''
    if len(get_indices(enc)) == 1:
        return ['']
    moves = get_moves(enc)
    res = []
    for move in moves:
        new_enc = list(enc)
        new_enc[move[0]] = '0'
        new_enc[move[1]] = '0'
        new_enc[move[2]] = '1'
        x = _cb_all(new_enc)
        for tup in x:
            z = move, *tup #unpacks the tuple and makes another
            res.append(z)
    return res

def cb_all(enc):
    '''
    Wrapper function for _cb_all.
    I'm not sure why _cb_all returns sets instead
    of arrays, but given that it works at all
    this is an easy fix. Calls _cb_all and returns
    an array full of an array of tuples.
    '''
    res = _cb_all(enc)
    new = []
    for i in res:
        new.append(list(i))
    return new