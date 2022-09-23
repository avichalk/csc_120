""" File: maze_solver.py
    Author: Avichal Kaul
    Purpose: Solves a maze for you if you're too lazy to solve it yourself.

    Comments: There's 300 lines of discarded code because it just. Would. Not. Work.
    I don't usually have moments of 'wow, I don't know how this code works'. I know
    where I messed up. Here, though, I can only assume it's witchcraft. It's not that
    I've done it wrong, I know I've done it right. It's more... why was it *this* attempt
    that worked and not any of my others? WHY?
    Edit: give Revo a raise please.
"""

class Tree:
    '''
    Creates a tree class that can store values,
    children and information about parents.
    '''
    def __init__(self, val, parent=None):
        '''
        self.parent stores the parent node.
        self.val stores the value
        self.up, self.down etc. store their respective nodes.
        '''
        self.parent = parent
        self.val = val
        self.up = None
        self.down = None
        self.left = None
        self.right = None

def main():
    '''
    Handles all our inputs, calls most of our functions.
    Does not return anything. Outputs a couple of error
    messages.
    '''
    filename = input()

    try:
        file = open(filename, 'r')
    except EOFError:
        return
    except:
        print(f'ERROR: Could not open file: {filename}')
        return

    lines, bad_file = file_processing(file)
    if bad_file:
        return

    path, start_end = list_processing(lines)
    start, end = find_start_end(start_end)
    start_node = tree_building(path, start_end)

    command = input()

    if command == 'dumpCells':
        dump_cells(path, start_end)
    elif command == 'dumpTree':
        print('DUMPING OUT THE TREE THAT REPRESENTS THE MAZE:')
        print_tree(start_node)
    elif command == 'dumpSize':
        wid, hei = dumpSize(path)
        print('MAP SIZE:')
        print(f'  wid: {wid}')
        print(f'  hei: {hei}')
    else:
        solution = find_in_tree(start_node, end) # before Revo's advice,
        if command == 'dumpSolution': # this function took so long that I
            dump_soln(solution) # put it here so it wouldn't cause runtime errors.
        elif command == '':
            wid, hei = dumpSize(path)
            soln(solution[1:-1], lines, wid)
        else:
            print(f'ERROR: Unrecognized command {command}')

def find_in_tree(root, val):
    '''
    Finds a path from the start of the tree (root)
    to a solution (val) using the nodes. Works now :D
    '''
    if root is None:
        return [0]
    if root.val == val:
        return [root.val]
    z = [0]
    up = find_in_tree(root.up, val)
    down = find_in_tree(root.down, val)
    left = find_in_tree(root.left, val)
    right = find_in_tree(root.right, val)
    if up[-1] == val:
       z = up
    elif down[-1] == val:
        z = down
    elif left[-1] == val:
        z = left
    elif right[-1] == val:
        z = right
    return [root.val] + z

def soln(solution, lines, wid):
    '''
    Prints our solution grid. Does not return anything.
    wid is the width of the grid, because spaces matter
    for some reason.
    '''
    print('SOLUTION:')
    new_lines = []
    for i in lines:
        x = list(i)
        new_lines.append(x)
    for point in solution:
        x = point[0]
        y = point[1]
        new_lines[y][x] = '.'
    for i in new_lines:
        my_str = ''
        for j in i:
            my_str += j
        while len(my_str) < wid:
            my_str += ' '
        print(my_str)

def dump_soln(solution):
    '''
    Dumps all points in our solution.
    Does not return anything.
    '''
    print('PATH OF THE SOLUTION:')
    for point in solution:
        print(f'  {point}')

def dumpSize(path):
    '''
    Takes a list, and returns the max
    x and y points in each tuple in that
    list.
    '''
    xmax = 0
    ymax = 0
    for point in path:
        if point[0] > xmax:
            xmax = point[0]
        if point[1] > ymax:
            ymax = point[1]
    return xmax+1, ymax+1

def print_tree(root, indent=''):
    '''
    Prints a pre-order traversal of our
    tree. Is recursive, so technically it will
    return None if the root passed to it is none.
    '''
    if root is None:
        return
    print(f'  {indent}{root.val}')
    if root.up is not None:
        print_tree(root.up, indent+'| ')
    if root.down is not None:
        print_tree(root.down, indent+'| ')
    if root.left is not None:
        print_tree(root.left, indent+'| ')
    if root.right is not None:
        print_tree(root.right, indent+'| ')

def dump_cells(path, start_end):
    '''
    Prints all the cells in the maze from the
    path list we got from the file. Does not return anything.
    '''
    print('DUMPING OUT ALL CELLS FROM THE MAZE:')
    start, end = find_start_end(start_end)
    for cell in sorted(path):
        if cell == start:
            print(f'  {cell}    START')
        elif cell == end:
            print(f'  {cell}    END')
        else:
            print(f'  {cell}')

def find_start_end(start_end):
    '''
    Finds the start and the end from our
    start_end dictionary. With the way I type
    reaching over to the inverted comma key
    is tedious, so I made this.
    '''
    return start_end['S'], start_end['E']

def tree_building(path, start_end):
    '''
    Recursive function that calls another private
    function to build a whole tree. Returns the root
    of that tree.
    '''
    start, end = find_start_end(start_end)
    start_node = Tree(start)
    _tree_building(start_node, path)
    return start_node

def _tree_building(node, path):
    '''
    Private recursive function that builds an entire
    tree recursively. Does not return anything (technically).
    Takes a node, the path along which to travel, and the end (goal).
    Such a nightmare, oh my god, send help.
    '''
    up, down, left, right = which_children(node, path)
    if not up and not down and not left and not right:
        return
    if up:
        point = (node.val[0], node.val[1]-1)
        node.up = Tree(tuple(point), parent=node)
        _tree_building(node.up, path)
    if down:
        point = (node.val[0], node.val[1]+1)
        node.down = Tree(tuple(point), parent=node)
        _tree_building(node.down, path)
    if left:
        point = (node.val[0]-1, node.val[1])
        node.left = Tree(tuple(point), parent=node)
        _tree_building(node.left, path)
    if right:
        point = (node.val[0]+1, node.val[1])
        node.right = Tree(tuple(point), parent=node)
        _tree_building(node.right, path)

def which_children(node, path):
    '''
    Takes a node and our path to figure out
    which children can be accessed (and aren't parents)
    Returns four booleans, one for each direction.
    '''
    if node is None:
        return False, False, False, False
    up = (node.val[0], node.val[1]-1)
    down = (node.val[0], node.val[1]+1)
    left = (node.val[0]-1, node.val[1])
    right = (node.val[0]+1, node.val[1])
    up_true, down_true, right_true, left_true = False, False, False, False
    if up in path:
        if node.parent is None or (node.parent is not None and node.parent.val != tuple(up)):
            up_true = True
    if down in path:
        if node.parent is None or (node.parent is not None and node.parent.val != tuple(down)):
            down_true = True
    if left in path:
        if node.parent is None or (node.parent is not None and node.parent.val != tuple(left)):
            left_true = True
    if right in path:
        if node.parent is None or (node.parent is not None and node.parent.val != tuple(right)):
            right_true = True
    return up_true, down_true, left_true, right_true

def list_processing(lines):
    '''
    Processes our file input list to ensure
    everything is in order, and returns the
    full path in the maze along with the
    start and the end points in a dictionary.
    '''
    path = []
    start_end = {}
    y = 0
    while y < len(lines):
        x = 0
        while x < len(lines[y]):
            if lines[y][x] == '#':
                path.append((x, y))
            if lines[y][x] in 'SE':
                path.append((x, y))
                start_end[lines[y][x]] = (x, y)
            x += 1
        y += 1
    return path, start_end

def file_processing(file):
    '''
    Processes our file upon init, and ensures it has the
    correct number of starting points, ending points,
    characters, etc. Returns a list of the lines in the file,
    and whether or not the file is bad.
    '''
    lines = [line.strip('\n') for line in file.readlines()]
    s_count = 0
    e_count = 0
    bad_file = False
    for line in lines:
        for char in line:
            if char == 'S':
                s_count += 1
            elif char == 'E':
                e_count += 1
            else:
                if char not in ' #':
                    print('ERROR: Invalid character in the map')
                    return [], True
    if s_count > 1:
       print('ERROR: The map has more than one START position')
       return [], True
    if e_count > 1:
        print('ERROR: The map has more than one END position')
        return [], True
    if s_count == 0 or e_count == 0:
        print('ERROR: Every map needs exactly one START and exactly one END position')
        return [], True
    return lines, bad_file

main()