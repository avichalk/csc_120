#! /usr/bin/python3

import grid_funcs


grid = [                     list(range(0,9)),
         list(range(9,10)) + list(range(0,8)),
         list(range(8,10)) + list(range(0,7)),
         list(range(7,10)) + list(range(0,6)),
         list(range(6,10)) + list(range(0,5)),
         list(range(5,10)) + list(range(0,4)),
         list(range(4,10)) + list(range(0,3)),
         list(range(3,10)) + list(range(0,2)),
         list(range(2,10)) + list(range(0,1)) ]

copy = grid_funcs.dup_grid(grid)

print("ORIGINAL:")
print(grid)
print()

print("COPY:")
print(copy)
print()

print("---- CHANGING THE COPY ----")
print()
copy[0][0] = 1234
copy[1][1] = 1234
copy[2][2] = 1234
copy[3][3] = 1234
copy[4][4] = 1234
copy[5][5] = 1234
copy[6][6] = 1234
copy[7][7] = 1234
copy[8][8] = 1234

print("ORIGINAL:")
print(grid)
print()

print("COPY:")
print(copy)
print()

print("TESTCASE COMPLETED")

