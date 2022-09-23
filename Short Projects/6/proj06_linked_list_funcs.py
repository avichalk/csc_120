from list_node import ListNode

def print_rev(head):
    ar = []
    while head is not None:
        ar.append(head.val)
        head = head.next
    x = len(ar) - 1
    while x >= 0:
        print(ar[x])
        x -= 1