#! /usr/bin/python3
import random
import graphics
FRAMES_PER_CYCLE = 120
FPS = 60
RADIUS = 10

class Vector:
    def __init__(self, x,y):
        self._x = x
        self._y = y
    def get(self):
        return self._x , self._y
    def __add__(self, other):
        assert type(other) == Vector
        return Vector( self._x + other._x,
                       self._y + other._y )
    def __mul__(self, k):
        assert type(k) in [int,float]
        return Vector( self._x * k,
                       self._y * k )
    def __sub__(self, other):
        assert type(other) == Vector
        return Vector( self._x - other._x,
                       self._y - other._y )

win = graphics.graphics(800,800, "Bezier Curve Demo")

p0 = Vector(100,400)
p1 = Vector(600,600)
p2 = Vector(600,100)
p3 = Vector(700,400)

AB = []
BC = []
ABC = []

t = 0
while not win.is_destroyed():
    def line(vec1,vec2, color="black", width=3):
        assert type(vec1) == Vector
        assert type(vec2) == Vector
        x1,y1 = vec1.get()
        x2,y2 = vec2.get()
        win.line(x1,y1, x2,y2, fill=color, width=width)

    def circle(center, radius, fill="black"):
        assert type(center) == Vector
        x,y = center.get()
        win.ellipse(x,y, radius,radius, fill=fill)

    win.clear()

    pA = p0 + (p1-p0)*(t/FRAMES_PER_CYCLE)
    pB = p1 + (p2-p1)*(t/FRAMES_PER_CYCLE)
    pC = p2 + (p3-p2)*(t/FRAMES_PER_CYCLE)

    line(p0,p1, width=1)
    line(p1,p2, width=1)
    line(p2,p3, width=1)

    circle(pA, RADIUS, "red")
    circle(pB, RADIUS, "red")
    circle(pC, RADIUS, "red")

    line(pA,pB, width=1)
    line(pB,pC, width=1)

    pAB = pA + (pB-pA)*(t/FRAMES_PER_CYCLE)
    pBC = pB + (pC-pB)*(t/FRAMES_PER_CYCLE)

    AB.append(pAB)
    BC.append(pBC)

    circle(pAB, RADIUS, "green")
    circle(pBC, RADIUS, "green")

    line(pAB,pBC, width=1)

    pABC = pAB + (pBC-pAB)*(t/FRAMES_PER_CYCLE)
    ABC.append(pABC)
    circle(pABC, RADIUS, "blue")

    for i in range(len(AB)-1):
        line( AB[i], AB[i+1], width=3, color="green")
        line( BC[i], BC[i+1], width=3, color="green")
        line(ABC[i],ABC[i+1], width=3, color="blue")

    win.update_frame(FPS)
    win.clear()
    t += 1
    if t > FRAMES_PER_CYCLE:
        win.clear()
        line(p0,p1, width=1)
        line(p1,p2, width=1)
        line(p2,p3, width=1)

        for i in range(len(ABC)):
            if i != 0:
                line(ABC[i-1],ABC[i], width=6, color="blue") # this one

        win.update_frame(.5)

        t = 0
        p0 = Vector( random.randint(0,800), random.randint(0,800) )
        p1 = Vector( random.randint(0,800), random.randint(0,800) )
        p2 = Vector( random.randint(0,800), random.randint(0,800) )
        p3 = Vector( random.randint(0,800), random.randint(0,800) )