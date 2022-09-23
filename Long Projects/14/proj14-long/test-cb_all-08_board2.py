#! /usr/bin/python3

import cb_solver



BOARD = "000011000000000"
assert len(BOARD) == 15



print("CALLING cb_all()...")
student = cb_solver.cb_all(BOARD)
print("DONE")
print()

print(f"STUDENT CODE RETURNED:")
for sol in sorted(student):
    print(f"  {sol}")

