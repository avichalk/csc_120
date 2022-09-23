# Question 2

class Corner:
    def __init__(self):
        self.up    = None
        self.down  = None
        self.left  = None
        self.right = None

def printer(param):
    print(id(param))
    print(id(param.up))
    print(id(param.down))
    print(id(param.left))
    print(id(param.right))

nw = Corner()
ne = Corner()
se = Corner()
sw = Corner()
nw.right = ne
ne.down  = se
se.left  = sw
sw.up    = nw
printer(nw)
printer(ne)
printer(sw)
printer(se)

# Question 4
class Corner:
    def __init__(self):
        self.up    = None
        self.down  = None
        self.left  = None
        self.right = None
    def printer(self):
        print(id(self))
        print(id(self.up))
        print(id(self.down))
        print(id(self.left))
        print(id(self.right))

# word of the day: corners