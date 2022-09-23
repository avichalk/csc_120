class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        head = self
        string = ''
        while head is not None:
            string += f'{head.val} '
            if head.next is not None:
                string += '<=> '
            head = head.next
        return string

def evens_to_list(data):
    new_arr = []
    for i in data:
        if i % 2 == 0:
            new_arr.append(i)
    return _evens_to_list(new_arr)

def _evens_to_list(new_arr):
    if len(new_arr) == 0:
        return None
    head = ListNode(new_arr[0])
    head.next = evens_to_list(new_arr[1:])
    return head

#print(evens_to_list([10,3,0,2]))

def mystery(head):
    maxim = 0
    while head is not None:
        assert head is not None
        assert head.next is not None
        val = abs(head.next.val-head.val)
        if val > maxim:
            maxim = val
        if head.next.next is not None:
            head = head.next
    return maxim

def do_something(head, new_node):
    if head.next is None:
        head.next = new_node
    else:
        new_node.next = head.next.next
        head.next.next = new_node

a = ListNode(10)
b = ListNode(-1)
c = ListNode(1024)
d = ListNode(0)
e = ListNode(123)

#print(mystery(a))

do_something(a, b)
do_something(a, c)
do_something(a, d)
do_something(a, e)
#print(a)