""" File: classes_prob2.py
    Author: Avichal Kaul
    Purpose: Contains a class Color,
    that can be used to store and edit
    rgb values.
"""

class Color:
    '''
    This class is made to contain some
    rgb values in such a way that they can be
    easily modified. The constructor takes the given
    rgb values (ensuring they are within the limits)
    and inits the object. Methods include:
        str(), which returns an rgb string_to_bytes
        html_hex_color(), which returns the rgb values in hexadecimal format
        get_rgb(), a getter for the rgb values
        remove_red(), which sets red to 0
        set_standard_color(name), which changes the rgb values to that of a standard
        colour.
    '''
    def __init__(self, r, g, b):
        r = self.limits(r)
        g = self.limits(g)
        b = self.limits(b)
        self._r = r
        self._g = g
        self._b = b

    def limits(self, val):
        if val < 0:
            val = 0
        if val > 255:
            val = 255
        return val

    def __str__(self):
        return str('rgb('+str(self._r)+','+str(self._g)+','+str(self._b)+')')

    def html_hex_color(self):
        return str('#'+str(f"{self._r:02X}")+str(f"{self._g:02X}")+str(f"{self._b:02X}"))

    def get_rgb(self):
        x = (self._r, self._g, self._b)
        return tuple(x)

    def set_standard_color(self, name):
        name1 = ''
        for i in name:
            name1 += i.lower()
        if name1 == 'white':
            self._r = 255
            self._g = 255
            self._b = 255
        if name1 == 'black':
            self._r = 0
            self._g = 0
            self._b = 0
        if name1 == 'red':
            self._r = 255
            self._g = 0
            self._b = 0
        if name1 == 'yellow':
            self._r = 255
            self._g = 255
            self._b = 0

    def remove_red(self):
        self._r = 0