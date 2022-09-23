def annoying_factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    if n == 4:
        return 4*annoying_factorial(3)
    if n == 5:
        return 5*annoying_factorial(4)
    if n == 6:
        return 6*annoying_factorial(5)
    if n > 6:
        return n*annoying_factorial(n-1)

def annoying_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return annoying_fibonacci(3)+annoying_fibonacci(2)
    if n == 5:
        return annoying_fibonacci(4)+annoying_fibonacci(3)
    if n == 6:
        return annoying_fibonacci(5)+annoying_fibonacci(4)
    if n > 6:
        return annoying_fibonacci(n-1)+annoying_fibonacci(n-2)

def annoying_climbUp(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 2, 3]
    if n == 4:
        z = annoying_climbUp(3)
        z.append(4)
        return z
    if n == 5:
        z = annoying_climbUp(4)
        z.append(5)
        return z
    if n == 6:
        z = annoying_climbUp(5)
        z.append(6)
        return z
    if n > 6:
        z = annoying_climbUp(n-1)
        z.append(n)
        return z

def annoying_climbDownUp(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [2, 1, 2]
    if n == 3:
        return [3, 2, 1, 2, 3]
    if n == 4:
        z = [4]
        z.extend(annoying_climbDownUp(3))
        z.append(4)
        return z
    if n == 5:
        z = [5]
        z.extend(annoying_climbDownUp(4))
        z.append(5)
        return z
    if n == 6:
        z = [6]
        z.extend(annoying_climbDownUp(5))
        z.append(6)
        return z
    if n > 6:
        z = [n]
        z.extend(annoying_climbDownUp(n-1))
        z.append(n)
        return z

