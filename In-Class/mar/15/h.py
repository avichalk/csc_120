from tree_node import TreeNode
import random

# Activity 1
def pretty_print_mod(root, indent=''):
    if root is None:
        return
    elif root.left is None:
        print(indent + str(root.val))
        pretty_print_mod(root.right, indent = indent+'  ')
        print(f"size() called on node {root.val}")
    elif root.right is None:
        print(indent + str(root.val))
        pretty_print_mod(root.left, indent = indent+'  ')
        x = tree_count(root.left)
        print(f"size() called on node {root.val}")
    elif root.right is None and root.left is None:
        print(indent + str(root.val))
        print(f"size() called on node {root.val}")
    else:
        print(indent + str(root.val))
        pretty_print_mod(root.right, indent = indent+'  ')
        pretty_print_mod(root.left, indent = indent+'  ')
        print(f"size() called on node {root.val}")
        print(f"size() called on node {root.val}")

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

# root = TreeNode(19)
# for i in range(0, 19):
#     root = random_insert(root)
#pretty_print_mod(root)
# it gets called a lot of times, usually multiple times on the same node. This might cause problems later.

# Activity 2
# root = TreeNode(13)
# root.left = TreeNode(26)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(80)

def fill_up_size_fields(root):
    if root is None:
        return 0
    size = 1
    if root.left is not None:
        fill_up_size_fields(root.left)
        size += root.left.size
    if root.right is not None:
        fill_up_size_fields(root.right)
        size += root.right.size
    root.size = size

# Activity 3
# In this case, the function would fail because some of the nodes would not have a size parameter associated with them.
class TreeNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None
        self.size = 1 # the initial value should be one because this node has no children inititally
# No we cannot, since the random tree building will add new nodes into spots where there were previously None, therefore causing our size parameter to display incorrect information.
def fill_up_size_fields_updated(root):
    if root is None:
        return 0
    else:
        if root.size is not None:
            return root.size
        root.size = 1 + fill_up_size_fields_updated(root.left) + fill_up_size_fields_updated(root.right)
        return root.size

# Word of the day : Caching

