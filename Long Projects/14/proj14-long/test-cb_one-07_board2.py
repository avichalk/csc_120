#! /usr/bin/python3

import sys
sys.path.insert(0, '..')

import cb_solver



BOARD = "000011000000000"
assert len(BOARD) == 15

VALID_SOLUTIONS = [ [(5, 4, 3)] ]



print("CALLING cb_one()...")
student = cb_solver.cb_one(BOARD)
print("DONE")
print()

if VALID_SOLUTIONS is None and student is None:
    print("SUCCESS!  Student correctly returned None.")
elif student in VALID_SOLUTIONS:
    print("SUCCESS!  Student code was in the set of solutions known to the testcase.")
else:
    print("FAIL!  The student solution was not in the set of known solutions.")
    print()
    print("STUDENT SOLUTION:")
    print(f"  {student}")
    print("KNOWN SOLUTIONS:")
    for sol in VALID_SOLUTIONS:
        print(f"  {sol}")

print()
print("TESTCASE ENDED")
