""" File: classes_prob1.py
    Author: Avichal Kaul
    Purpose: contains a couple of classes
    that you can do fun things with.
"""


class Simplest:
    '''
    This class constructs a couple of variables.
    '''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    '''
    This class takes three variables, makes them
    attributes to an object. Methods include:
        getter for first, second and third
        rotate(), which swaps all their places
        in a cyclical fashion.
    '''
    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

    def get_third(self):
        return self._third

    def rotate(self):
        num_1 = self._first
        self._first = self._second
        self._second = self._third
        self._third = num_1

class Band:
    '''
    This class represents a band. You can pass it
    members of the band, and it will store them.
    The constructor inits the singer, drummer and set of guitarists.
    Methods include:
        getters and setters for singers and drummers and guitar players.
        fire_all_guitar_players(), which fires all guitarists
        play_music(), which prints some music to screen depending on the
        singer, the number of guitar players, and if the band has a drummer.
    '''
    def __init__(self, singer):
        self._singer = singer
        self._drummer = None
        self._guitar = []

    def get_singer(self):
        return self._singer

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_drummer(self):
        return self._drummer

    def set_drummer(self, new_drummer):
        self._drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self._guitar.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self._guitar = []

    def get_guitar_players(self):
        guita = []
        for i in self._guitar:
            guita.append(i)
        return guita

    def play_music(self):
        if self._singer == 'Frank Sinatra':
            print('Do be do be do')
        elif self._singer == 'Kurt Cobain':
            print('bargle nawdle zouss')
        else:
            print('La la la')
        if self._drummer != None:
            print('Bang bang bang!')
        print('Strum!\n'*len(self._guitar), end = '')