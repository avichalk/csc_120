""" File: linked_list_recursion_part2.py
    Author: Avichal Kaul
    Purpose: Has lots of linked list recursion functions.
"""

from list_node import ListNode

def array_to_list_recursive(data):
    '''
    Takes an array as input and
    returns a linked list with all
    the nodes containing values in the
    array.
    '''
    if data == []:
        return
    else:
        head = ListNode(data[0])
        new_head = array_to_list_recursive(data[1:])
        head.next = new_head
        return head

def accordion_recursive(head):
    '''
    Removes every second value in a linked
    list and returns said list.
    '''
    if head is None:
        return None
    elif head.next is None:
        return None
    else:
        head = head.next
        if head.next is not None:
            head.next = accordion_recursive(head.next)
        return head

def pair_recursive(head1, head2):
    '''
    Recurses through two linked lists
    at the same time and returns a linked
    list with both values as a tuple in
    each node.
    '''
    if head1 is None or head2 is None:
        return
    else:
        tup = head1.val, head2.val
        cur = ListNode(tuple(tup))
        cur.next = pair_recursive(head1.next, head2.next)
        return cur