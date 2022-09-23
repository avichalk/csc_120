# Activity 1
# the nodes will always have less value than than
# the new node.
cur = head
while cur.val <= cur.next.val:
    cur = cur.next()

# Activity 2
# if you get them out of order,
# the new node value is lost.
cur.next().next() = cur
cur = cur.next()

# Activity 3
# if you get it backwards, it won't work if
# the list is empty
if head is None:
	Head = new_node
elif head.val > new_node.val:
	New_node.next = head
	Head = new_node

# Activity 4
cur = head
while cur.val <= cur.next.val:
    cur = cur.next()