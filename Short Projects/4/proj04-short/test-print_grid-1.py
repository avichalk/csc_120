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

grid_funcs.print_grid(grid)
print("TESTCASE COMPLETED")

