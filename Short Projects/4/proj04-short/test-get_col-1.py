#! /usr/bin/python3

import grid_funcs


grid = [ [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ],
         [ 0 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 ],
         [ 2 , 3 , 5 , 7 , 11, 13, 17, 19, 23],
         [ 29, 31, 37, 41, 43, 47, 53, 59, 61],
         [ 67, 71, 73, 79, 83, 89, 97,101,103],
         [107,109,113,119,141,143,149,151,157],
         [161,163,167,171,173,177,187,191,193],
         [199,203,209,211,217,221,223,227,229],
         [233,239,241,247,251,253,257,261,263] ]


print(sorted(grid_funcs.get_col(grid, 0)))
print(sorted(grid_funcs.get_col(grid, 1)))
print(sorted(grid_funcs.get_col(grid, 3)))
print(sorted(grid_funcs.get_col(grid, 8)))

print("TESTCASE COMPLETED")

