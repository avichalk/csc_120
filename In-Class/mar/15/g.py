from tree_node import TreeNode
import random

# Activity 1
def pretty_print(root, indent=''):
    if root is None:
        return
    elif root.left is None:
        print(indent + str(root.val))
        pretty_print(root.right, indent = indent+'  ')
    elif root.right is None:
        print(indent + str(root.val))
        pretty_print(root.left, indent = indent+'  ')
    elif root.right is None and root.left is None:
        print(indent + str(root.val))
    else:
        print(indent + str(root.val))
        pretty_print(root.right, indent = indent+'  ')
        pretty_print(root.left, indent = indent+'  ')

# Activity 2
def random_insert(T):
    v = random.randint(0, 100)
    #x = random.randint(1, 2)
    if T == None:
        return TreeNode(v)
    elif v % 2 == 0:
        T.left = random_insert(T.left)
    elif v % 2 != 0:
        T.right = random_insert(T.right)
    return  T

# Activity 3
def pretty_print_mod(root, indent=''):
    if root is None:
        return
    elif root.left is None:
        print(indent + str(root.val))
        pretty_print_mod(root.right, indent = indent+'  ')
        x = tree_count(root.right)
        print(x)
    elif root.right is None:
        print(indent + str(root.val))
        pretty_print_mod(root.left, indent = indent+'  ')
        x = tree_count(root.left)
        print(x)
    elif root.right is None and root.left is None:
        print(indent + str(root.val))
        print(1)
    else:
        print(indent + str(root.val))
        pretty_print_mod(root.right, indent = indent+'  ')
        pretty_print_mod(root.left, indent = indent+'  ')
        x = tree_count(root.right)
        print(x)
        x = tree_count(root.left)
        print(x)

def tree_count(root):
    '''
    Takes a tree as a parameter
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

# the problem is caused by lots of recursion.
# WOTD: Timezones