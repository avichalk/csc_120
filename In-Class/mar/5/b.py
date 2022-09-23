# wotd: log of n
# Activity 1
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

i = [10, 20, 15, 16, 17, 19, 33, 44, 50, 100, 200]
root = TreeNode(i[0])
root.lchild = TreeNode(i[1])
root.rchild = TreeNode(i[2])
root.lchild.lchild = TreeNode(i[3])
root.rchild.rchild = TreeNode(i[4])
root.lchild.rchild = TreeNode(i[5])
root.rchild.lchild = TreeNode(i[6])
root.lchild.lchild.lchild = TreeNode(i[7])
root.rchild.rchild.rchild = TreeNode(i[8])
root.lchild.rchild.lchild = TreeNode(i[9])
root.rchild.lchild.rchild = TreeNode(i[10])

i = [20, 10, 16, 15, 19, 17, 44, 33, 100, 50, 200]
root = TreeNode(i[0])
root.lchild = TreeNode(i[1])
root.rchild = TreeNode(i[2])
root.lchild.lchild = TreeNode(i[3])
root.rchild.rchild = TreeNode(i[4])
root.lchild.rchild = TreeNode(i[5])
root.rchild.lchild = TreeNode(i[6])
root.lchild.lchild.lchild = TreeNode(i[7])
root.rchild.rchild.rchild = TreeNode(i[8])
root.lchild.rchild.lchild = TreeNode(i[9])
root.rchild.lchild.rchild = TreeNode(i[10])

# they are not the same tree, they do not have the same root, and these trees are not balanced
# activity 2

no1 = [17, 44, 200, 50, 100, 19, 33, 10, 20, 15, 16]
no2 = [16, 10, 50, 200, 19, 20, 44, 33, 100, 17, 15]
no3 = [44, 16, 100, 17, 20, 10, 50, 33, 15, 19, 200]

# we ran out of time for activity 3





import random
i = [20, 10, 16, 15, 19, 17, 44, 33, 100, 50, 200]
ar = []
y = 0
while y < 10:
    x = random.randint(0, 10)
    if x not in ar:
        temp = i[y]
        i[y] = i[x]
        i[x] = temp
        ar.append(x)
    y += 1