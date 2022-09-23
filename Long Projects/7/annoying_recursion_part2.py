""" File: annoying_recursion_part2.py
    Author: Avichal Kaul
    Purpose: Contains a multitude of annoying recursive functions
"""

def annoying_triangleNumbers(n):
    '''
    Calculates the nth triange number
    recursively.
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6
    if n == 4:
        return 4+annoying_triangleNumbers(3)
    if n == 5:
        return 5+annoying_triangleNumbers(4)
    if n == 6:
        return 6+annoying_triangleNumbers(5)
    if n > 6:
        return n+annoying_triangleNumbers(n-1)

def annoying_fibonacci_sequence(n):
    '''
    Returns an array full of fibbonaci
    numbers up until the nth fibbonaci
    number recursively.
    '''
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    if n == 3:
        return [0,1,1]
    if n == 4:
        z = annoying_fibonacci_sequence(3)
        z.append(z[-1]+z[-2])
        return z
    if n == 5:
        z = annoying_fibonacci_sequence(4)
        z.append(z[-1]+z[-2])
        return z
    if n == 6:
        z = annoying_fibonacci_sequence(5)
        z.append(z[-1]+z[-2])
        return z
    if n > 6:
        z = annoying_fibonacci_sequence(n-1)
        z.append(z[-1]+z[-2])
        return z

def annoying_valley(n):
    '''
    Prints a valley to screen
    recursively.
    '''
    if n == 0:
        print()
    if n == 1:
        print('*')
    if n == 2:
        print('./')
        print('*')
        print('.\\')
    if n == 3:
        print('../')
        print('./')
        print('*')
        print('.\\')
        print('..\\')
    if n == 4:
        print('.'*(4-1)+'/')
        annoying_valley(3)
        print('.'*(4-1)+'\\')
    if n == 5:
        print('.'*(5-1)+'/')
        annoying_valley(4)
        print('.'*(5-1)+'\\')
    if n == 6:
        print('.'*(6-1)+'/')
        annoying_valley(5)
        print('.'*(6-1)+'\\')
    if n > 6:
        print('.'*(n-1)+'/')
        annoying_valley(n-1)
        print('.'*(n-1)+'\\')