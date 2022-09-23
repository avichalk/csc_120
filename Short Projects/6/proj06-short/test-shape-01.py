#! /usr/bin/python3


import proj06_shape



def main():
    print("Checking that proj06_shape() returns the proper structure")
    L = proj06_shape.proj06_shape()


    if len(L) != 2:
        print(f"ERROR: incorrect list length on the root node (expected: 2; got: {len(L)})")
    if len(L[0]) != 2 or len(L[0][0]) != 2 or len(L[0][0][0]) != 2:
        print("ERROR: incorrect list length on one of the top-row nodes (other than the root node)")

    if L[0][0][0][0] is not None:
        print("ERROR: The length of the top row is incorrect.")

    if type(L) != list or type(L[0]) != list or type(L[0][0]) != list or type(L[0][0][0]) != list:
        print("ERROR: One of the four top-row nodes is not an array object.")


    def check_col(col_root, col_num):
        if                                col_root         [1] is     None or \
           len(col_root[1]      ) != 2 or col_root      [1][1] is     None or \
           len(col_root[1][1]   ) != 2 or col_root   [1][1][1] is     None or \
           len(col_root[1][1][1]) != 2 or col_root[1][1][1][1] is not None:
            print(f"ERROR: One of the elements in column {col_num} has the wrong length, or has the wrong value in [1]")

        if col_root[1]      [0] != (col_num,0) or \
           col_root[1][1]   [0] != (col_num,1) or \
           col_root[1][1][1][0] != (col_num,2):
            print(f"ERROR: One of the elements in column {col_num} has the wrong value in [0]")

    check_col(L,          0)
    check_col(L[0],       1)
    check_col(L[0][0],    2)
    check_col(L[0][0][0], 3)


    print()
    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

