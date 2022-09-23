from tree_node import TreeNode

# wotd: perfect BSTs

# Activity 1
def pretty_print_mod(root, indent=''):
    if root is None:
        return
    else:
        pretty_print_mod(root.left, indent = indent+'  ')
        print(indent + str(root.val))
        pretty_print_mod(root.right, indent = indent+'  ')
        print(f"size() called on node {root.val}")
# Activity 2
'''
We think that the tree will often be unbalanced, because the first element of the array
is the root that determines how balanced the tree will end up being and it is chosen
randomly.
'''

def array_to_tree(array):
    tree = None
    for i in array:
        tree = tree_insert(tree)
    return tree

def tree_insert(T):
    if T == None:
        return TreeNode(v)
    elif v < T.val:
        T.left = tree_insert(T.left)
    elif v > T.val:
        T.right = tree_insert(T.right)
    return  T

' After running some tests, we found that we were correct. '
# Activity 3
def array_to_tree(array):
    tree = None
    for i in array:
        tree.left = TreeNode(i)
        tree = tree.left
    return tree

# Activity 4
def array_to_tree(array):
    tree = None
    tree = _array_to_tree(sorted(array), tree)
    return tree
def _array_to_tree(array, tree):
    x = int(len(array)/2)
    tree = TreeNode(array[x])
    for i in array[:x]:
        tree.left = _array_to_tree(array[:x], tree.left)
    for j in array[x+1:]:
        tree.right = _array_to_tree(array[x+1:], tree.right)
    return tree



