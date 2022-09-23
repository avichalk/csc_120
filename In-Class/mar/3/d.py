#Activity 1
'''
root- It's the node at the top of the tree.(Only one root)

Leaf - is the node which doesn't have any children.
There can be multiply leaves.

child - A node that is connected to one parent

parent - A node that is connected to one or more children.

binary tree - A tree that each parent node has two children.
'''
#Activity 2
'''
It's not a tree since the leaf node which has value 18
has 2 parents.
'''
#Activity 3

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

root = TreeNode(24)
root.lchild = TreeNode(12)
root.rchild = TreeNode(36)
root.lchild.lchild = TreeNode(10)
root.lchild.rchild = TreeNode(15)
root.rchild.lchild = TreeNode(25)
root.rchild.rchild = TreeNode(40)

#Activity 5
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

def mystery(root):
    if root is None:
        return 0
    if root.lchild is None and root.rchild is None:
        return 1
    else:
        return mystery(root.lchild) + mystery(root.rchild)

root = TreeNode(24)
root.lchild = TreeNode(12)
root.rchild = TreeNode(36)
root.lchild.lchild = TreeNode(10)
root.lchild.rchild = TreeNode(15)
root.rchild.lchild = TreeNode(25)
root.rchild.rchild = TreeNode(40)

print(mystery(root))

Wotd: binary