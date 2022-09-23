from time import time

# Activity 1

def mystery_one(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

# this is a bubble sort function.
# it has runtime complexity O(1)

# Activity 2

# def call_append(maxim):
#     x = 100
#     data = []
#     while x < maxim:
#         start = time()
#         for i in range(x):
#             data.append(i)
#         end = time()
#         print(f'{x}: {end-start}')
#         x = x * 10
# call_append(1000000000)

# with each 10x increase in size, the time increases by 10.
# so this might be an O(n) function.

# Activity 3

def string_append(string, maxim):
    start = time()
    for i in range(maxim):
        string += str(i)
    end = time()
    print(f'{maxim}: {end-start}')
x = 10
while x < 100000000000:
    string_append('string', x)
    x = x * 10

# as we can see, the cost goes up with each 10x increase
# more than in append. So, adding to a string is more
# costly than appending to an array.
# (the code for the next one still hasn't finished running)