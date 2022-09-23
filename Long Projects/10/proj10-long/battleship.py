""" File: battleship.py
    Author: Avichal Kaul
    Purpose: Lets you play a game of battleship
    using two classes that interact with each other.

    Comments: This was surprisingly painless! Apart from
    the bottom row of the print function for two digits,
    I hated that. Still, no major refactoring! No ten hours
    of debugging! (yet. I haven't actually checked it on
    gradescope because I'm too nervous).
    Edit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    why is the test so goddamn long you literally cannot tell
    what's going wrong and oh god what is it doing to my poor
    code why is it going so wrong what did i miss
    Edit 2: fixed it.
"""

class Board:
    '''
    Builds a board on which you can play a game of battleship.
    Takes only one size param, because the board will always be
    a square.
    '''
    def __init__(self, size):
        '''
        self.map is a 2D list that always has a graphical
        representation of the entire board's state.
        self.size is an integer that is the size of the board.
        self.ship_pos is a dictionary that has the ship object as the key
        and the position of the ship on the board as a list of tuples as the
        item.
        self.used is a list containing all the points on the board that have
        been hit by the players.
        '''
        assert size > 0
        self.map = [['.' for i in range(size)] for i in range(size)]
        self.size = size
        self.ship_pos = {}
        self.used = []

    def print(self):
        '''
        The offset refers to the number of spaces
        that need to be left for the decoration
        pieces and numbers along the bottom.
        This function takes no params, and goes
        into two other print helper functions.
        '''
        offset = 1
        if self.size > 10:
            offset = 2
        self.print_grid(offset)
        self.print_bottom(offset)

    def print_grid(self, offset):
        '''
        Prints the grid and the numbers along the
        left. Takes the offset for the decorations
        anaw. z is just an iter variable. Does some
        weird things with f strings. Does not return
        anything. I didn't notice the extra spacing at
        first and it tripped me up, but thankfully
        it was a quick fix.
        '''
        z = self.size-1
        print(' '+' '*offset+'+'+'-'*(self.size*2+1)+'+')
        for i in self.map:
            string = ''
            for j in i:
                string += j
                string += ' '
            if offset == 2:
                if z < 10:
                    print(f" {z} | {string}|")
                else:
                    print(f"{z} | {string}|")
            else:
                print(f"{z} | {string}|")
            z -= 1
        print(' '+' '*offset+'+'+'-'*(self.size*2+1)+'+')

    def print_bottom(self, offset):
        '''
        The most frustrating part of this project,
        which is thankfully not saying much. It does
        need a function all to itself so it can work.
        Does some super weird things, does not return
        anything. Uses offset to offset from the left.
        '''
        # code for the tens place
        if self.size > 10:
            amount = 0
            numbers_str = '  '
            while amount < self.size:
                tens = amount // 10
                if tens != 0:
                    numbers_str += str(tens)
                    numbers_str += ' '
                else:
                    numbers_str += '  '
                amount += 1
            print(' '+' '*offset + numbers_str)
        # code for the ones place
        other_numbers_str = ''
        amount = self.size
        while amount >= 0:
            for i in range(0, 10):
                other_numbers_str += str(i)
                other_numbers_str += ' '
            amount -= 1
        print('   '+' '*offset + other_numbers_str[:self.size*2-1])

    def add_ship(self, ship, position):
        '''
        Adds a ship. Takes the ship object and its
        position on the board as parameters. Asserts
        some things, processes the coordinates, and if
        everything is correct, it adds it onto the board.
        Does not return anything.
        '''
        ship.position = position
        pos = []
        for point in ship.shape:
            coord = [sum(coord) for coord in zip(point, position)]
            pos.append(tuple(coord))  # adds the points in the ship shape
            # to the position, thus giving each point's position on the
            # board which is stored in pos.
        for ship_name in self.ship_pos:
            for occupied_point in self.ship_pos[ship_name]:
                for new_ship_point in pos:
                    assert new_ship_point != occupied_point
        self.ship_pos[ship] = pos
        for position in pos:
            x, y = self.range_calc(position)
            self.map[self.size-y-1][x] = ship.name[0].upper()  # adds ship letter

    def has_been_used(self, position):
        '''
        Returns true or false depending on whether or not
        the position has been used before. Takes a tuple/
        list with 2 indices as a param.
        '''
        x, y = self.range_calc(position)
        if position in self.used:
            return True
        return False

    def attempt_move(self, position):
        '''
        Attempts a move. If the place hasn't
        already been hit, it goes ahead and hits it.
        It also checks if the ship has sunk on each
        hit. If the position does not have a ship at it,
        it replaces the . with an o. Returns a string
        describing what has happened.
        '''
        x, y = self.range_calc(position)
        ship_is_sunk = False
        assert position not in self.used
        for ship in self.ship_pos:
            for point in self.ship_pos[ship]:
                if position == point:
                    self.map[self.size-y-1][x] = '*'
                    self.used.append(position)
                    ship_is_sunk = ship.ship_hit(point)
                    if ship_is_sunk:
                        ship.sink_ship(self)
                        return f'Sunk ({ship.name})'
                    return 'Hit'
        self.map[self.size-y-1][x] = 'o'
        self.used.append(position)
        return 'Miss'

    def range_calc(self, position):
        '''
        Takes a tuple/list with two
        integers, asserts they are within
        the ranges of the board, then returns
        them individually.
        '''
        x = position[0]
        y = position[1]
        assert y in range(self.size)
        assert x in range(self.size)
        return x, y

class Ship:
    '''
    Is a ship you can place onto a board to play a game
    of battleship. It takes a string as a name, and a list
    of points as a shape.
    '''
    def __init__(self, name, shape):
        '''
        self.name is a string containing the ship name.
        self.sunk is a bool that is false upon init, but
        becomes true once the ship is sunk.
        self.shape contains a list of tuples of the points
        making up the ship
        self.hits is the number of times the ship has been hit.
        if self.hits equals the length of self.shape, the ship is
        sunk.
        self.indexes_hit is a list containing the indexes of the points
        where the ship was hit so we can print it out.
        self.position is a tuple of the position of the ship on the board,
        used to pinpoint the exact bit of the ship that was struck. it should
        be unnessecary, but just in case something goes wrong it's there.
        '''
        self.name = name
        self.sunk = False
        self.shape = shape
        self.hits = 0
        self.indexes_hit = []
        self.position = 0

    def ship_hit(self, point):
        '''
        If the ship is hit, it calls this function. point is the point on the board when
        the ship was hit. We find the xy coord in terms of self.shape, iter through self.shape
        and find the point that was hit, and mark off its index. If the ship is sunk, it
        updates self.sunk to be true. It returns self.sunk.
        '''
        x = point[0] - self.position[0]
        y = point[1] - self.position[1]
        ship_hit_point = x, y
        i = 0
        while i < len(self.shape):
            if self.shape[i] == tuple(ship_hit_point):
                self.indexes_hit.append(i)
            i += 1
        self.hits += 1
        if self.hits == len(self.shape):
            self.sunk = True
        return self.sunk

    def print(self):
        '''
        Prints the ship out, noting if points have
        been hit or not. Does not return anything.
        '''
        print_str = ''
        i = 0
        while i < len(self.shape):
            if i in self.indexes_hit:
                print_str += '*'
            else:
                print_str += self.name[0].upper()
            i += 1
        print_str += ' '*(10-len(print_str))
        print_str += self.name
        print(print_str)

    def sink_ship(self, board):
        '''
        If the ship is sunk, it changes all the bits on the
        board to reflect this. Takes the board object as a
        param, does not return anything.
        '''
        for ship in board.ship_pos:
            if ship == self:
                for point in board.ship_pos[ship]:
                    board.map[board.size-point[1]-1][point[0]] = 'X'

    def is_sunk(self):
        '''
        Getter for self.sunk
        '''
        return self.sunk

    def rotate(self, amount):
        '''
        Rotates the ship by changing the points
        in self.shape. Does not return anything,
        takes a param amount that is an int b/w
        0 and 3 inclusive.
        '''
        shape_array = []
        for point in self.shape:
            x = point[0]
            y = point[1]
            new_point = x, y
            if amount == 1:
                new_point = y, -x
            if amount == 2:
                new_point = -x, -y
            if amount == 3:
                new_point = -y, x
            shape_array.append(tuple(new_point))
        self.shape = shape_array