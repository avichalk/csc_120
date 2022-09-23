#! /usr/bin/python3

import cb_solver



BOARD = "000011000000000"
assert len(BOARD) == 15


print("CALLING print_board()...")
cb_solver.print_board(BOARD)
print("DONE")


