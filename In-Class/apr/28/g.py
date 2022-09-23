# WOTD: TOYOTA
import random
from time import time
# Activity 1
class ArrayStack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if self.stack == []:
            return True
        return False
    def push(self, val):
        assert val is not None
        self.stack.append(val)
    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        return val

z = ArrayStack()
def push_rand(stack, n):
    for i in range(n):
        stack.push(random.randint(0, 100))

def pop_all(stack, n):
    for i in range(n):
        stack.pop()

# init and is_empty take very little time. now to check push and pop

# start = time()
# push_rand(z, 100000)
# print(f'push took {time()-start}')

# start = time()
# pop_all(z, 100000)
# print(f'pop took {time()-start}')

# push took about 10x longer, but pop is taking much, much longer. this is because of array slicing.

# Activity 2
# If we do this, then each time we want to add something we will have to recurse to the end of the list.
# Each time we want to pop something, we will have to do the same.
# The head of the list should be the newest node, so any newer nodes can be added instantly and any popping
# also takes no time at all.

# Activity 3
class ListStack:
    def __init__(self):
        self.stack = None
        self.next = None
    def is_empty(self):
        if self.stack == None:
            return True
        return False
    def push(self, val):
        assert val is not None
        new = ListNode(val)
        new.next = self.stack
        self.stack = new
    def pop(self):
        val = self.stack.next
        self.stack = val
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

z = ListStack()
z.push(10)
z.push(20)
#z.pop()
print(z.stack.val) # Looks like it works. It's cost should be around O(1), since we're only doing one or two operations independent of the size of the linked list.
