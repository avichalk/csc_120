#! /usr/bin/python3

""" Code to test the tree_sum() function

    Author: Russ Lewis
"""

import tree_funcs



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)
root.left = TreeNode(52)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing tree_sum()...")
    print()

    retval = tree_funcs.tree_sum(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


