""" File: grid_funcs.py
    Author: Avichal Kaul
    Purpose: Is a grid of functions
    that will be very useful to us
    in our next long project.
"""

def arr_of_strs_to_2d_array(strs):
    new_strs = []
    for x in range(9):
        arr_var = []
        for y in range(9):
            arr_var.append(strs[y][x])
        new_strs.append(arr_var)
    return new_strs

def print_grid(grid):
    j = 0
    for y in range(9):
        i = 0
        str_var = ''
        for x in range(9):
            if grid[x][y] == 0:
                str_var += '.'
            else:
                str_var += str(grid[x][y])
            i += 1
            if i == 3:
                i = 0
                str_var += ' '
        print(str_var)
        j += 1
        if j == 3:
            j = 0
            print()

def dup_grid(grid):
    new_grid = []
    for i in grid:
        grid_var = []
        for j in i:
            grid_var.append(j)
        new_grid.append(grid_var)
    return new_grid


def get_row(grid, x):
    array = []
    for y in range(9):
        array.append(grid[y][x])
    return array

def get_col(grid, y):
    array = []
    for x in range(9):
        array.append(grid[y][x])
    return array

def get_square(grid, xy, sx):
    '''
    The instructions I was given for the parameters
    turned out to be wrong, which is why they're flipped.
    '''
    xy = 3*xy
    x = xy + 3
    arr = []
    while xy < x:
        z = 3*sx
        y = z + 3
        while z < y:
            arr.append(grid[xy][z])
            z += 1
        xy += 1
    ar = []
    return arr
