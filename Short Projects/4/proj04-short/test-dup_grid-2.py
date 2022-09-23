#! /usr/bin/python3

import grid_funcs


grid = [ [1]*9,
         [2]*9,
         [3]*9,
         [4]*9,
         [5]*9,
         [6]*9,
         [7]*9,
         [8]*9,
         [9]*9 ]

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

