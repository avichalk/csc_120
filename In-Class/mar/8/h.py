import random
# Activity 1
def print_tree(root):
    if root is None:
        return
    else:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)
# Activity 2
# Tree 2 is out of order, therefore not a BST.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

tree1 = TreeNode(74)
tree1.left  = TreeNode(4)
tree1.right = TreeNode(80)
tree1.left.left  = TreeNode(0)
tree1.left.right = TreeNode(17)
tree1.right.left  = TreeNode(77)
tree1.right.right = TreeNode(96)
tree2 = TreeNode(69)
tree2.left  = TreeNode(38)
tree2.right = TreeNode(63)
tree2.left.left  = TreeNode(53)
tree2.left.right = TreeNode(68)
tree2.right.left  = TreeNode(88)
tree2.right.right = TreeNode(46)

#print_tree(tree1)
#print_tree(tree2)

# Activity 3
def height_of_tree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    if root.right is None:
        return 1+height_of_tree(root.left)
    if root.left is None:
        return 1+height_of_tree(root.right)
    else:
        if height_of_tree(root.right) > height_of_tree(root.left):
            z = height_of_tree(root.right)
        else:
            z = height_of_tree(root.left)
        return 1+z
# x = height_of_tree(tree1)
# print(x)

# Activity 4

def height_of_tree(root):
    if root is None:
        return -1
    else:
        if height_of_tree(root.right) > height_of_tree(root.left):
            z = height_of_tree(root.right)
        else:
            z = height_of_tree(root.left)
        return 1+z

# x = height_of_tree(tree1)
# print(x)

# Word of the day - DEPTH

# Challenge
def insert(T, v):
    if T == None:
        return TreeNode(v)
    if v < T.val:
        T.left = insert(T.left, v)
    elif v > T.val:
        T.right = insert(T.right, v)
    return T

root = None
i = 0
while i < 999:
    i = i+1
    rand_value = random.randint(-5*1000,20*1000)
    root = insert(root, rand_value)

x = height_of_tree(root)
print(x)