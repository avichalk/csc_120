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
root.right = TreeNode(52)
root.right.left = TreeNode(12)
root.right.left.right = TreeNode(66)
root.right.left.right.left = TreeNode(50)
root.right.left.right.left.left = TreeNode(-31)
root.right.left.right.left.left.right = TreeNode(81)
root.right.left.right.left.left.right.right = TreeNode(-6)
root.right.left.right.left.left.right.right.right = TreeNode(77)



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


