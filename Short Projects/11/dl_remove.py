from dlist_node import DListNode

def dl_remove(head, node):
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    if node.prev is None:
        head = head.next
        if node.next is None:
            head = None
    return head