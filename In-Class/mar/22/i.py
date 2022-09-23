# WOTD : breakpoint

# Activity 1
def print_items(lst):
    for item in lst:
        print(item)

print("Printing out a list")
new_list = [4, 8, 12]
print_items(new_list)
print("Done")

# lines 8, 9, 10, 5, 6, 5, 6, 5, 6, 5, 11 will run in that order

# Activity 2
print('a')
print('b')
print('c')
print('d')
print('e')
# breakpoints stop the code from running at a certain point.
# print(c) and print(e) did not run until we pressed continue
# the code reaches a breakpoint and stops to await further instructions

# Activity 3
def print_items(lst):
    for item in lst:
        print(item)

print("Printing out a list")
new_list = [4, 8, 12]
print_items(new_list)
print("Done")
# in step in, we go through each line of the function
# in step over, we skip over the function and wait on
# the next line. we could use step over when we know
# that a function works and we want to check the code
# around it.

# Activity 4
# it got cleaned up because it was unreferenced.

# Activity 5
def foo(num1, num2):
    return num1 * num2
def bar(str, num):
    return str[num]
a = 3
b = 4
c = foo(a, b)
z = "Hello   World"
out = bar(z, c)
print(out)

# We just add two spaces to z, because originally a*b was too long.