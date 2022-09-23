from list_node import ListNode

grid = '11'
new_grid = '13'


def stack_init(grid):
    ''
    head = ListNode(grid)
    return head

def stack_addition(new_grid, head):
    ' how to do the linkedlist? idk'
    new_node = ListNode(new_grid)
    old = head
    head = ListNode(new_grid)
    #print(head)
    head.next = old
    return head

def stack_deletion(head):
    if head.next != None:
        cur = head.next
    else:
        cur = head
    return cur

def testing(grid, new_grid):
    head = stack_init(grid)
    head = stack_deletion(head)
    print(head)
    head = stack_deletion(head)

testing(grid, new_grid)