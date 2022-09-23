""" File: twine.py
    Author: Avichal Kaul
    Purpose: Helps the user navigate
    through a maze.
    Comments: Mercy please oh my god this was such
    a nightmare.
"""

def main():
    '''
    Handles some of the initialization, such as the obstacle file input,
    the stack, and calling some other programs. It also handles one (1) error.
    '''
    print('Please give the name of the obstacles filename, or - for none:')
    ob_file = input()

    stack, stack_pos = stack_init()

    if ob_file == '-':
        ob_list = []
    elif ob_file == '':
        print('ERROR: Filename blank')
        ob_list = []
    else:
        ob_list = obstacles(stack, stack_pos, ob_file)

    program_run(stack, stack_pos, ob_list)

def stack_init():
    '''
    Initializes the stack. It's mostly here for testing purposes.
    Also, I really like this function. It doesn't throw any errors.
    It wasn't the result of seven hours of difficult, confusing work.
    It doesn't just stop working at random. It's nice and simple.
    I can change it and it won't break.
    It's not stack_change_for_map or write_twine_func.
    This is my favourite function in the entire program.
    '''
    stack = [(0,0)]
    stack_pos = len(stack)
    return stack, stack_pos

def program_run(stack, stack_pos, ob_list):
    '''
    This is our main function. It calls most other functions,
    depending on the user input, and is recursive.
    '''

    cur_pos = stack[stack_pos-1]
    # the current position will always be the last thing in the stack

    prompt(cur_pos, stack)
    command, command_var = user_input(cur_pos, stack, stack_pos)
    if command_var == 1:  # if the user inputs a direction
        new_pos = direction_processing(cur_pos, command, stack, stack_pos)
        stack, stack_pos, new_pos = \
        stack_processing(new_pos, stack, stack_pos, ob_list)
    elif command_var == 2:  # if the user inputs back
        stack, stack_pos = back_process(stack, stack_pos)
    elif command_var == 3:  # crossings
        crossings(stack, cur_pos)
    elif command_var == 4:  # map
        map_func(stack, cur_pos, ob_list)
    elif command_var == 5:
        ranges(stack)  # ranges
    program_run(stack, stack_pos, ob_list)

def obstacles(stack, stack_pos, ob_file):
    '''
    This handles the obstacles initialization.
    If anything goes wrong, it spits out an error
    and returns an empty list to main.
    '''
    try:
        oblist = open(ob_file, 'r').readlines()
    except:
        print('ERROR: File does not exist')
        program_run(stack, stack_pos, [])
    ob_list = []
    try:
        for i in oblist:
            i = i.strip('\n').split(' ')
            k = []
            for j in i:
                k.append(int(j))
            ob_list.append(tuple(k))  # ensures data in this
            # list is consistent
    except:    # with the rest of the program.
        print('ERROR: Invalid data.')  # This was surprisingly horrid.
    return ob_list

def ranges(stack):
    '''
    The ranges function. It does not return anything,
    just prints the extreme values of the stack.
    '''
    stack = list(set(stack))
    x_coord = []
    y_coord = []
    for i in stack:
        x_coord.append(i[0])
        y_coord.append(i[1])
    print('The furthest West your twine goes is', min(x_coord))
    print('The furthest East your twine goes is', max(x_coord))
    print('The furthest South your twine goes is', min(y_coord))
    print('The furthest North your twine goes is', max(y_coord))



def write_twine_func(other_stack_list, \
    cur_pos_list, i, origin_is_cur_pos, ob_list):
    '''
    This handles all of our printing, and was by far
    the worst part of this program. We print the program
    one line at a time and left to right, so we need to
    completely change the stack. This is handled by a later
    function. Then we have to ensure the program knows where
    it has to print full stops, spaces, asterisks, the like.
    That was also awful. There's around 100 lines of discarded
    code that didn't work.
    '''
    ob_list = sorted(ob_list) # i think the sorted() is helping? maybe?
    k=1
    string_var = ''  # this is each line of the map.
    while k<12:  # k is the x value of the map and by extension the string.
        x = 0  # i should've called it x and used k for the other thing
        j = 0  # but it's too late now anyways.
        while x<(len(other_stack_list[i])):  # it's a while loop and not
            if other_stack_list[i][x] == k:  # a for loop because of how
                if i == cur_pos_list[1]:  # data is stored in other_stack_list.
                   if k == cur_pos_list[0]:  # checks if we are at
                        string_var+='+'  # current position
                        j+=1
                        break
                if i == 6:  # checks if we are at origin
                    if k == 6:
                        if origin_is_cur_pos!=1:  # checks that origin is
                            string_var+='*'  # not the current position. if
                            j+=1  # it is, we've already printed a +
                            break
                for h in ob_list:  # checks if we are at an obstacle
                    if i == 6-h[1]:
                        if k == h[0]+6:
                            string_var+='X'
                            j+=1
                            break
                else:  # if none of these are true,  the only things left
                    string_var+='.'  # in the stack are the twine.
                x+=1
                j+=1
            else:
                x+=1
        if j == 0:  # if none of the above happened, it means there's
            string_var+=' '  # nothing corresponding to that position
        k+=1  # in the stack. it prints a blank space.
    return string_var


def map_func(stack, cur_pos, ob_list):
    '''
    Also a disaster. The entire map section of this
    assignment is an unmitigated disaster actually.

    Essentially, it prints everything to screen line
    by line in that big i loop. We need to have everything processed
    and waiting, otherwise it'll mess up during printing. It
    calls stack_change_for_map, because we had to change the
    structure of the entire stack and also add the obstacles to it.
    It also calls write_twine_func because the string changes
    every line. It does not return anything.
    '''
    other_stack_list, cur_pos_list = \
    stack_change_for_map(stack, cur_pos, ob_list)
    print('+-----------+')
    origin_is_cur_pos = 0
    if cur_pos_list == [6,6]:  # if the current position of the player
        origin_is_cur_pos = 1  # is at the origin, we set this variable as 1.
        # it's a secret tool that will help us later!
    i = 1
    while i<=11:  # y-value of the map. yes, I should've called it y and not i.
        string = '|'
        string_var = write_twine_func(other_stack_list, \
        cur_pos_list, i, origin_is_cur_pos, ob_list)
        string+=string_var
        string+='|'
        print(string)
        i+=1
    print('+-----------+')  # fun fact: this was originally a 70 line function.

def stack_change_for_map(stack, cur_pos, ob_list):
    '''
    This function changes the structure of the stack.
    The star of the show is other_stack_list. Unlike
    the stack, which keeps track of position chronologically
    and in relation to the origin, this list stores position
    by y-value (because that's how we have to print it out)
    and in relation to the edges of the map. The x and y
    values change completely and remain completely
    incompatible with the rest of the program. Also,
    other_stack_list[0] has nothing in it. It goes from
    1 to 11 because that's how the y-values are stored
    and that's how they have to be printed out. It returns
    other_stack_list and cur_pos_list, which contains the
    current position in this new format.

    Most of this jankiness is my fault, but some of
    it is also because of an aliasing bug. If I hadn't watched
    the playposit video, I would've torn my hair out.
    '''
    stack_list = []
    stack_new = []
    for i in stack:  # this right here is where the aliasing bug was, officer
        stack_new.append(i)
    for i in ob_list:  # adds obstacle coordinates to the new list.
        stack_new.append(i)
    stack_new_new = list(set(stack_new))  # removes duplicates.
    for i in stack_new_new:
        stack_list_list = []
        stack_list_list.append(int(i[0]+6))
        stack_list_list.append(12-int(i[1]+6))
        stack_list.append(stack_list_list)
    cur_pos_list = []
    cur_pos_list.append(cur_pos[0]+6)
    cur_pos_list.append(6-cur_pos[1])
    # this bit above changes the x and y values to be in terms of the edges of the map
    # and not the origin. the origin, incidentally, is now (6,6)
    other_stack_list = [[]]*12
    i=1
    while i<12:
        stack_var = []
        for j in stack_list:
            if j[1] == i:
                stack_var.append(j[0])  # if the y-value is equal to the index of the list,
        other_stack_list[i] = stack_var  # the x value is added into a list that's then added
        i+=1  # into the index position. It means that each index position contains a list of
        # x-positions for that y-value/index position.
    # this is because if there were two things on the same line, they'd get all messed up while printing.
    # i tried to fix it, but it was unsalvageable. bye bye, approx 60 lines of code.
    # as a happy coincidence, anything that's not on the grid gets discarded! and the function is exactly 30 lines!!!
    return other_stack_list, cur_pos_list


def crossings(stack, cur_pos):
    '''
    Calculates the number of crossings.
    '''
    i=0
    for j in stack:
        if j == cur_pos:
            i+=1
    print('There have been', i, 'times in the history when you were at this point.')


def stack_processing(new_pos, stack, stack_pos, ob_list):
    '''
    Processes the stack and adds new values to it if the user decides to make a move.
    If there are obstacles in the way, it tells the user that it cannot move.

    I sure am glad I put this in its own function,
    because it was very useful when implementing obstacles.
    '''
    if new_pos not in ob_list:
        stack.append(new_pos)
        stack_pos+=1
    else:
        print('You could not move in that direction, because there is an obstacle in the way.\nYou stay where you are.')
        new_pos = stack[len(stack)-1]
    return stack, stack_pos, new_pos

def back_process(stack, stack_pos):
    '''
    Moves the user back, unless they're at the start, in which case it refuses.
    '''
    if len(stack) > 1:
        stack.pop()
        stack_pos-=1
        print('You retrace your steps by one space')
    elif len(stack) == 1:
        print("Cannot move back, as you're at the start!")
    return stack, stack_pos



def prompt(cur_pos, stack):
    '''
    This is the prompt that shows up after every command.
    '''
    print()
    print('Current position:', cur_pos)
    print('Your history:    ', stack)
    print('What is your next command?')



def user_input(cur_pos, stack, stack_pos):
    '''
    This handles all our user input and most of our errors.
    It returns what the user commanded, and what the user wants to do.
    These are different because for all commands in command_list_2,
    there is only one set of functions to be called.
    '''
    try:
        command = input()
    except:
        exit()

    command_list_1 = ['', 'back', 'crossings', 'map', 'ranges']
    command_list_2 = ['n', 's', 'e', 'w']

    test_1 = command.split(' ')

    command_var = 0
    if len(test_1) > 1:
        print('ERROR: More than one word typed.')
    elif command in command_list_1:
        if command == '':
            print('You do nothing.')
        if command == 'back':
            command_var = 2
        if command == 'crossings':
            command_var = 3
        if command == 'map':
            command_var = 4
        if command == 'ranges':
            command_var = 5
    elif command in command_list_2:
        command_var = 1
    else:
        print('ERROR: Command not recognised')

    return command, command_var

def direction_processing(cur_pos, command, stack, stack_pos):
    '''
    Takes the direction the user wants to go in and processes it,
    returning the new_pos of the user as a neat little tuple :).
    '''
    x = cur_pos[0]
    y = cur_pos[1]
    if command == 'n':
        y+=1
    if command == 's':
        y-=1
    if command == 'e':
        x+=1
    if command == 'w':
        x-=1
    new_pos = (x,y)
    return new_pos


main()