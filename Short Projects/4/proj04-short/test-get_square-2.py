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


print(sorted(grid_funcs.get_square(grid, 2,2)))
print(sorted(grid_funcs.get_square(grid, 1,2)))
print(sorted(grid_funcs.get_square(grid, 0,0)))
print(sorted(grid_funcs.get_square(grid, 2,0)))

print("TESTCASE COMPLETED")

