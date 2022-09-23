""" File: sudoku_helper.py
    Author: Avichal Kaul
    Purpose: Helps the player play
    a relaxing game of sudoku with
    linked lists and such.
    Comments: If, once I'm done with
    this class, I never see a gradescope
    autograder ever again, it will be too
    soon. Good god.
    Also, I have no idea what the x and y
    conventions for this program are.
"""
from list_node import ListNode

def main():
    '''
    Our main function handles our file input,
    initializes the grid and the stack, and
    passes the grid and the head through to
    another function.
    '''
    print('Please give the name of the file that contains the board:', end='')
    fi_name = input()
    grid = import_grid(fi_name)
    head = stack_init(grid)
    user_input(grid, head)

def stack_init(grid):
    '''
    My finest work. Creates a listnode,
    and returns it.
    '''
    head = ListNode(grid)
    return head

def print_grid(grid):
    '''
    This prints the grid to screen
    in the format we're expected to
    use. It does not return anything.
    '''
    j = 0
    for y in range(9):
        i = 0
        z = 0
        str_var = ''
        for x in range(3):
            for k in grid[y][x]:  # yes, the x being after the y
                if k == '0':  # was confusing. It's because of the
                    str_var += '.'  # way the listdata is stored.
                else:
                    str_var += str(k)
                i += 1
            if i == 3:
                i = 0
                z += 1
                if z != 3:
                    str_var += ' '
        print(str_var)
        j += 1
        if j == 3:
            j = 0
            print()

def handles_answers(grid):
    '''
    This function creates a dictionary,
    then loops through all x and y
    values from 0 to 9 and passes them
    through to another function that
    figures out what the possible answers are.
    It adds these lists of possible answers to
    a dictionary with key 'xy'. Then, depending
    on the answers we got, we print something.
    It does not return anything.
    '''
    answers = {}
    z = 0
    for y in range(9):
        for x in range(9):
            ans = possible_answers(grid, x, y)
            answers[f'{x}{y}'] = ans
    for coord in answers:
        if len(answers[coord]) == 1:  # for one solution
            z += 1
            print(f'Solution! The only value possible at square {coord[0]+1}, {coord[1]+1} is {answers[coord][0]}.')
        if len(answers[coord]) == 0:  # for no solutions
            print(f'The square {coord[0]+1}, {coord[1]+1} does not have any possible values!')
    if z == 0:  # if there aren't solutions found for any of the squares
        print('Sorry, no solutions were found.')

def possible_answers(grid, x, y):
    '''
    This accepts x and y values from
    0 to 9 and uses them to iterate
    through our list to find which values
    are still possible answers for a specific
    square.
    '''
    answers = []
    square = []
    column = []
    row = []
    for i in range(1, 10):
        answers.append(i)
    x_simp, x_simp_add, y_simp, y_simp_add = simp(x, y)
    inner_x, inner_y = inner_peace(x, y)
    if grid[y][x_simp][inner_x] == '0':
        square = subregion_to_array(grid, int(x/3), int(y/3))
        column = search_vertically(grid, x, y)
        row = search_horizontally(grid, x, y)
    for i in square:
        if i in answers:
            answers.remove(i)
    for i in column:
        if i in answers:
            answers.remove(i)
    for i in row:
        if i in answers:
            answers.remove(i)
    return answers

def user_input(grid, head):
    '''
    This is our recursive function
    that calls itself over and over
    again. It decides which functions
    to call based on user input.
    It does not return anything.
    '''
    print()
    print_grid(grid)
    print('Your command:\n')
    command = command_thing()
    if command == '':
        command = command_thing()
    if command.split(' ')[0] == 'set':
        new_grid = xy_value_changer(grid, head, command)
        head = stack_addition(new_grid, head)
        grid = new_grid
    elif command == 'conflicts':
        conflicts(grid)
    elif command == 'search':
        handles_answers(grid)
    elif command == 'back':
        head = stack_deletion(head)
        grid = head.val
    else:
        print('ERROR: Invalid command')
    user_input(grid, head)

def command_thing():
    '''
    This quits if we reach the end of the file
    I think, I'm not sure.
    '''
    try:
        command = input()
    except:
        quit()
    return command

def stack_addition(new_grid, head):
    '''
    This function adds to our linked
    list. head.val is the newest value,
    and the entire list is returned through
    head.
    '''
    new_node = ListNode(new_grid)
    old = head
    head = ListNode(new_grid)
    head.next = old
    return head

def stack_deletion(head):
    '''
    This deletes the most recent addition
    to our linked list, unless it's the only
    thing in the list in which case it refuses.
    '''
    if head.next != None:
        cur = head.next
    else:
        cur = head
        print('ERROR: You are already at the init state, you cannot go back.')
    return cur

def import_grid(fi_name):
    '''
    This function imports the grid
    and also handles filenotfound
    errors. Sort of. I think. It
    returns an array with all our
    data inside.
    '''
    x = 0
    try:
        file = open(fi_name, 'r')
    except FileNotFoundError:
        print('\nERROR: The file could not be opened.')
        x = 1
    if x == 1:
        quit()
    lines = file.readlines()
    arr = []
    for i in lines:
        i = i.strip()
        i = i.replace('.', str(0))
        if i != '':
            arr.append(i.split(' '))
    return arr

def xy_value_changer(grid, head, command):
    '''
    This changes the value of a square inside
    our grid to be something else, unless there's
    already a value set at that position, in which
    case it refuses.
    '''
    x = command.split(' ')[1]
    y = command.split(' ')[2]
    new_val = command.split(' ')[3]
    x = int(x)-1
    y = int(y)-1
    inner_x, inner_y = inner_peace(int(x), int(y))
    x_simp, x_simp_add, y_simp, y_simp_add = simp(int(x), int(y))
    new_grid = dup_grid(grid)
    thing = list(new_grid[int(y)][x_simp])
    if thing[inner_x] != '0':
        print("ERROR: The 'set' command cannot run, because the space already holds a value.")
        user_input(grid, head)
    else:
        thing[inner_x] = str(new_val)
        str_var = ''
        for i in thing:
            str_var += i
        new_grid[int(y)][x_simp] = str_var
        print(f'Square {x+1},{y+1} set to {new_val}.')
        return new_grid

def dup_grid(grid):
    '''
    This duplicates a grid to avoid
    an aliasing bug.
    '''
    new_grid = []
    for i in grid:
        grid_var = []
        for j in i:
            grid_var.append(j)
        new_grid.append(grid_var)
    return new_grid

def unused_digits(array):
    '''
    Takes a list of strings in sudoku format,
    converts them into individual ints. Checks
    to see which are unused, puts them in an array
    and returns them.
    '''
    arr = []
    for i in array:
        for j in i:
            arr.append(int(j))
    ar = []
    for j in range(1, 10):
        ar.append(j)
    for i in arr:
        if i in ar:
            ar.remove(i)
    return ar

def no_duplicates(array):
    '''
    Makes sure there aren't duplicates
    in the array. If there are, it'll
    be evident in the dup_set it returns.
    '''
    dup = [0]*10
    dup_set = set()
    for i in array:
        if i != 0:
            dup[int(i)] += 1
        for m, k in enumerate(dup):
            if k > 1:
                dup_set.add(m)
    return dup_set


def conflicts(grid):
    '''
    Checks to see if there's any conflicts
    in the grid by going through the entire
    thing. It does not return anything, instead
    just printing messages to the user if there's
    a conflict.
    '''
    x = 0
    y = 0
    z = 0
    dup_1_issues = set()
    dup_2_issues = set()
    for y in range(9):  # this is for the rows and columns
        for x in range(9):
            ver = search_vertically(grid, x, y)
            hor = search_horizontally(grid, x, y)
            dup_1 = no_duplicates(ver)
            if dup_1 != set():
                dup_1_issues.add(x+1)
            dup_2 = no_duplicates(hor)
            if dup_2 != set():
                dup_2_issues.add(y+1)
    for i in dup_1_issues:
        print('ERROR: Column', i, 'has a conflict.')
        z+=1
    for i in dup_2_issues:
        print('ERROR: Row', i, 'has a conflict.')
        z+=1
    x = 0
    y = 0
    while y < 3:  # this is for the subregions
        for x in range(3):
            arr = subregion_to_array(grid, x, y)
            dup_3 = no_duplicates(arr)
            if dup_3 != set():
                print(f'ERROR: Sub-region {x+1}, {y+1} has a conflict.')
                z+=1
        y +=1
    if z == 0:
        print('Hooray!  No conflicts found.')


def search_vertically(grid, x, y):
    '''
    Takes x and y coord and returns all
    values in the column it is in.
    '''
    x_simp, x_simp_add, y_simp, y_simp_add = simp(x, y)
    inner_x, inner_y = inner_peace(x, y)
    ar = []
    i = 0
    while i < 9:
        if grid[i][x_simp][inner_x] != '0':
            ar.append(int(grid[i][x_simp][inner_x]))
        i += 1
    return ar

def inner_peace(x, y):
    '''
    We have an outer iterator (x) and an inner.
    the outer goes through the grid, the inner
    goes through the strings inside the grid.
    It calculates these iterators and returns them.
    I genuinely do not know what inner_y is for,
    but I'm going to leave it in because I'm not
    physically or emotionally ready for this program
    to break.
    '''
    inner_x = x
    while inner_x >= 3:
        inner_x -= 3
    inner_y = y
    while inner_y >= 3:
        inner_y -= 3
    return inner_x, inner_y

def search_horizontally(grid, x, y):
    '''
    Searches the row a given square is in,
    puts all the values in it into an array,
    and returns it. I should note all these
    functions take x and y values from 0 to 9.
    I think. It might be 0 to 8.
    '''
    x_simp, x_simp_add, y_simp, y_simp_add = simp(x, y)
    inner_x, inner_y = inner_peace(x, y)
    ar = []
    for j in grid[y]:
        for k in j:
            if k != '0':
                ar.append(int(k))
    return ar


def small_square(grid, x, y):
    '''
    Gets all the numbers in a square and puts them
    into an array it returns.
    '''
    x_simp, x_simp_add, y_simp, y_simp_add = simp(x, y)
    arr = []
    while x_simp < x_simp_add:
        arr.append(grid[x_simp][y_simp])
        x_simp += 1
    return arr

def subregion_to_array(grid, x, y):
    '''
    Unlike the others, this takes x and y from 0 to 3.
    It gets all the numbers from a subregion and puts
    them into an array.
    '''
    x_simp, x_simp_add, y_simp, y_simp_add = simp_for_square(x, y)
    arr = []
    while y_simp < y_simp_add:
        j = grid[y_simp][x].strip('0')
        if j != '':
            arr.append(j)
        y_simp += 1
    ar = []
    for i in arr:
        for j in i:
            if j != '0':
                ar.append(int(j))
    return ar

def simp_for_square(x, y):
    '''
    Serves the same purpose as simp, but exclusively
    for subregions. The other one doesn't work for
    subregions.
    '''
    x_simp = 3*x
    y_simp = 3*y
    x_simp_add = x_simp + 3
    y_simp_add = y_simp + 3
    return x_simp, x_simp_add, y_simp, y_simp_add

def simp(x, y):
    '''
    Simplifies our x and y values. We don't
    need the y simplified, I don't know why I
    did this but fixing it will take too long.
    Since our inner operator (inner_x) goes from
    0 to 3, our outer operator (x) will have to
    be simplified so it can work.
    '''
    x_simp = int(x/3)
    x_simp_add = x_simp + 3
    y_simp = int(y/3)
    y_simp_add = y_simp + 3
    return x_simp, x_simp_add, y_simp, y_simp_add

main()