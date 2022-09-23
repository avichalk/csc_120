from dlist_node import DListNode

def dl_insert_before(head, node, insert):
    insert.next = node
    insert.prev = node.prev
    if node.prev is not None:
        node.prev.next = insert
    if node.prev is None:
        head = insert
    node.prev = insert
    return head

def dl_insert_after(head, node, insert):
    insert.prev = node
    insert.next = node.next
    if node.next is not None:
        node.next.prev = insert
    node.next = insert
    return head
