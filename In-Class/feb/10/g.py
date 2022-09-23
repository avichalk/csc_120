# Activity 1
cur = head
while cur.val < cur.next.val:
    cur = cur.next

# Activity 2
new_node.next = cur.next
cur.next = new_node

# Activity 3
if head is None:
    head = new_node
if new_node.val < head.val:
    new_node.next = head
    head = new_node

# Activity 4
cur = head
while cur.next is not None:
    cur = cur.next
new_node.next = cur.next
cur.next = new_node

# Word of the day : there isn't one whoops-a-daisy