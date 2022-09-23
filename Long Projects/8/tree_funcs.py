""" File: tree_funcs.py
    Author: Avichal Kaul
    Purpose: contains functions for trees
"""

from tree_node import TreeNode

def tree_count(root):
    '''
    Takes a tree root as a parameter
    and returns the number of nodes
    in it.
    '''
    if root is None:
        return 0
    elif root.left is None:
        return 1 + tree_count(root.right)
    elif root.right is None:
        return 1 + tree_count(root.left)
    elif root.left is None and root.right is None:
        return 1
    else:
        return 1 + tree_count(root.left) + tree_count(root.right)

def tree_count_1_child(root):
    '''
    Takes a tree root as a parameter and
    returns the number of nodes with
    exactly one child.
    '''
    if root is None:
        return 0
    elif root.right is None and root.left is None:
        return 0
    else:
        if root.right is not None and root.left is not None:
            return tree_count_1_child(root.right) + tree_count_1_child(root.left)
        else:
            if root.right is not None:
                return 1 + tree_count_1_child(root.right)
            if root.left is not None:
                return 1 + tree_count_1_child(root.left)

def tree_sum(root):
    '''
    Takes a tree as a param and returns the sum
    of all the values in it.
    '''
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.val
    else:
        if root.left is not None and root.right is not None:
            return tree_sum(root.left) + tree_sum(root.right) + root.val
        else:
            if root.left is not None:
                return root.val + tree_sum(root.left)
            if root.right is not None:
                return root.val + tree_sum(root.right)

def tree_print(root):
    '''
    Prints all the values in a tree
    in no particular order.
    Takes a tree root as a parameter.
    '''
    if root is None:
        return
    else:
        print(root.val)
        if root.right is not None:
            tree_print(root.right)
        if root.left is not None:
            tree_print(root.left)

def tree_print_leaves(root):
    '''
    Takes a tree root as a parameter and
    prints all the leaves in it.
    '''
    if root is None:
        return
    elif root.left is None and root.right is None:
            print(root.val)
    else:
        if root.right is not None:
            tree_print_leaves(root.right)
        if root.left is not None:
            tree_print_leaves(root.left)

def bst_search_loop(root, val):
    '''
    Takes a bst root and a value as
    parameters, searches through the tree
    and returns either None or the node
    containing the value.
    '''
    while root is not None:
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        elif root.val < val:
            root = root.right
    return None

def tree_search(root, val):
    '''
    Takes a tree root and a value as parameters,
    searches through the tree for the value
    and returns it.
    '''
    if root is None:
        return
    elif root.val == val:
        return root
    else:
        x = None
        y = None
        if root.right is not None:
            x = tree_search(root.right, val)
        if root.left is not None:
            y = tree_search(root.left, val)
        if x is not None:
            return x
        else:
            return y

def tree_max(root):
    '''
    Takes a tree root as a parameter,
    finds the maximum value in it
    and returns it.
    '''
    if root is None:
        return
    else:
        val = root.val
        if root.left is not None:
            x = tree_max(root.left)
            if x > val:
                val = x
        if root.right is not None:
            x = tree_max(root.right)
            if x > val:
                val = x
        return val

def bst_max_loop(root):
    '''
    Takes a bst root as a parameter,
    finds the maximum value in it
    and returns it.
    '''
    while root.right is not None:
        root = root.right
    return root.val