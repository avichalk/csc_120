def myfunc(v):
    return [v[0]]
x = myfunc([10,20])
print(x)

def myfunc1():
    return ['ab', 'cd', 'ef']

def myfunc2():
    a = [20,30]
    return [10, a]

def myfunc3(x,y):

    y[1] = x
    x[1] = y
    return x

# Ques 5
One checks to see if they have the same
numeric value, while the other checks to see
if they are the same object.

# Word of the day - KEYBOARD