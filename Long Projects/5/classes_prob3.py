""" File: classes_prob3.py
    Author: Avichal Kaul
    Purpose: Contains a class (Room)
    and a function build_grid (plus
    subsidiaries). These help create
    a group of linked rooms that can
    be accessed from one another.
"""

class Room:
    '''
    This class creates a room in a maze.
    It contains exits and a unique name
    for each room. The constructor sets all
    the exits to None and creates a unique name.
    There are several useful methods:
        get_name(): returns the name of the room
        set_name(name): sets a name for the room
        collapse_room(): collapses a room, and ensures
        no other rooms can get to it.
    '''
    def __init__(self, x, y, x_max, y_max):
        self.n = None
        self.w = None
        self.e = None
        self.s = None
        self._name = str(str(x)+' ' +str(y)+'name')

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) is str:
            self._name = name

    def collapse_room(self):
        if self.n is not None:
            self.n.s = None
            self.n = None
        if self.w is not None:
            self.w.e = None
            self.w = None
        if self.e is not None:
            self.e.w = None
            self.e = None
        if self.s is not None:
            self.s.n = None
            self.s = None

def build_grid(width, height):
    '''
    Builds a grid using our class Room.
    Each room object is interconnected
    with others through its exits. It uses
    two other functions to build horizontally
    and vertically. It returns the southwest
    corner of the grid.
    '''
    grid = []
    x = 0
    while x < width:
        y = 0
        ar = []
        while y < height:
            z = Room(x, y, width, height)
            ar.append(z)
            y += 1
        grid.append(ar)
        x += 1
    grid = build_x(grid, width, height)
    grid = build_y(grid, width, height)
    return grid[0][0]

def build_x(grid, width, height):
    '''
    Builds our room grid horizontally.
    Returns an array filled with references to room
    objects.
    '''
    x = 0
    while x < width:
        if x != 0:
            y = 0
            while y < height:
                grid[x][y].w = grid[x-1][y]
                y += 1
        if x != width-1:
            y = 0
            while y < height:
                grid[x][y].e = grid[x+1][y]
                y += 1
        x += 1
    return grid

def build_y(grid, width, height):
    '''
    Builds our room grid vertically.
    Returns an array filled with references to room
    objects.
    '''
    y = 0
    while y < height:
        if y != 0:
            x = 0
            while x < width:
                grid[x][y].s = grid[x][y-1]
                x += 1
        if y != height-1:
            x = 0
            while x < width:
                grid[x][y].n = grid[x][y+1]
                x += 1
        y += 1
    return grid