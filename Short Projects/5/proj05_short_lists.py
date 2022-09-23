from list_node import ListNode
import math

def list_to_array(head):
    ''
    ar = []
    while head is not None:
        ar.append(head.val)
        head = head.next
    return ar

def array_to_list(array):
    ''
    if len(array) == 0:
        head = None
        return head
    else:
        i = 1
        head = ListNode(array[0])
        cur = head
        while i < len(array):
            cur.next = ListNode(array[i])
            cur = cur.next
            i += 1
        return head

def list_length(head):
    ''
    z = 0
    while head is not None:
        head = head.next
        z += 1
    return z

def split_list(head):
    ''
    if head == None:
        return None
    else:
        z = list_length(head)
        z = z/2
        z1 = math.ceil(z)
        z2 = int(z)
        cur = head
        i = 1
        while i < z1:
            cur = cur.next
            i += 1
        new = cur.next
        cur.next = None
        x = head, new
        x = tuple(x)
        return x

