# WOTD: UGTA (undergraduate teaching assistant)

import random

# Activity 1
def gen_rand(n):
    array = []
    print('starting array')
    for i in range(n):
        array.append(random.randint(0, 100))
    print('array is done')
    return array

# Activity 2
x = gen_rand(1000000). # this takes a while
# this might be O(n^2)

# Activity 3
def sum_array(array):
    all_sum = 0
    print('starting sum')
    for i in array:
        all_sum += int(i)
    print('sum is done')
    return all_sum

# We think it will be O(n)

x = gen_rand(1000000)
y = sum_array(x)
print(y)

# it seems like O(n) is correct

# Activity 4
# The first will cause a stack overflow, because we recurse too much, because the list is so huge.
# In the second, the slice is very expensive. With n turned down, we can tell the time is almost
# exponential. So it is O(e^n)