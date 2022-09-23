# No WOTD since this is split across two ICAs
# new WOTD: mapping
# Activity 1

class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def shallow_word(tree, letter):
    return _shallow_word(tree, letter)[0]

def _shallow_word(root, letter, depth=0):
    if root is None:
        return (None, depth)
    else:
        if root.val == letter:
            return (root, depth)
        else:
            x = _shallow_word(root.left, letter, depth+1)
            y = _shallow_word(root.right, letter, depth+1)

            if x[0] is not None and y[0] is not None:
                if x[1] < y[1]:
                    return x
                else:
                    return y

            if y is None:
                return x
            if x is None:
                return y

# Activity 2
def print_dfs(root):
    q = [root]
    white len(q) != 0:
        deq = q.pop(0)
        if deq.left is not None:
            q.append(deq.left)
        if deq.right is not None:
            q.append(deq.right)
        for e in q:
            print(e.val)

# Activity 3
def print_dfs(root, letter):
    q = [root]
    white len(q) != 0:
        deq = q.pop(0)
        if deq.val == letter:
            return deq
        if deq.left is not None:
            return q.append(deq.left, letter)
        if deq.right is not None:
            return q.append(deq.right, letter)