from list_node import ListNode

def is_sorted(head):
    if head == None:
        return True
    if head.next == None:
        return True
    while head is not None and head.next is not None:
        if head.val > head.next.val:
            return False
        head = head.next
    return True

def is_sorted_recursive(head):
    if head == None:
        return True
    if head.next == None:
        return True
    if head is not None and head.next is not None:
        if head.val > head.next.val:
            return False
    return True and is_sorted_recursive(head.next)