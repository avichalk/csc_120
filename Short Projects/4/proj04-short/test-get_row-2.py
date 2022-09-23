#! /usr/bin/python3

import grid_funcs


grid = [ list("abcdefghi"),
         list("jklmnopqr"),
         list("stuvwxyz "),
         list("Stars!isa"),
         list("noldgamet"),
         list("hatIloveb"),
         list("butthegra"),
         list("phicsaret"),
         list("errible  ") ]


print(sorted(grid_funcs.get_row(grid, 2)))
print(sorted(grid_funcs.get_row(grid, 3)))
print(sorted(grid_funcs.get_row(grid, 4)))
print(sorted(grid_funcs.get_row(grid, 5)))

print("TESTCASE COMPLETED")

