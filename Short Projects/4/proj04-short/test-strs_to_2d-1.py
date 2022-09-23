#! /usr/bin/python3

import grid_funcs


strs = [ "abcdefghi",
         "ghijklmno",
         "---------",
         "|||||||||",
         "         ",
         ".........",
         "123456789",
         "xxxxxxxxx",
         "ooooooooo" ]

print(grid_funcs.arr_of_strs_to_2d_array(strs))
print("TESTCASE COMPLETED")

