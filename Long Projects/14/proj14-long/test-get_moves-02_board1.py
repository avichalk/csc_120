#! /usr/bin/python3

import cb_solver



BOARD = "010101010101010"
assert len(BOARD) == 15


print("CALLING get_moves()...")
moves = cb_solver.get_moves(BOARD)
print("DONE")

print("STUDENT CODE RETURNED:")
for move in sorted(moves):
    print(f"  {move}")

print("TESTCASE ENDED")


