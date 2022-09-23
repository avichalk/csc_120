from list_insert import *
from dlist_utils import *
from dlist_node import DListNode

'dlist utils things'

def test_dlist_is_consistent():
    # case 1 - head = None
    head = None
    dlist_is_consistent(head)

    # case 2 - head.prev is not None
    head = DListNode(12)
    head.prev = DListNode(10)
    dlist_is_consistent(head)

    # case 3 - cur/prev mismatch\
    def case_three():
        # case 3.1
        head = DListNode(12)
        node_1 = DListNode(10)
        node_2 = DListNode(8)
        head.next = node_1
        node_1.prev = node_2
        dlist_is_consistent(head)
        # case 3.2 - node.prev is None
        head = DListNode(12)
        node_1 = DListNode(10)
        head.next = node_1
        node_1.prev = None
        dlist_is_consistent(head)
    case_three()

    # case 4 - good linked list
    head = DListNode(12)
    node_1 = DListNode(10)
    head.next = node_1
    node_1.prev = head
    dlist_is_consistent(head)

test_dlist_is_consistent()

def test_dlist_to_str():
    # case 1 - head = None
    head = None
    print(dlist_to_str(head))

    # case 2 - infinite
    head = DListNode(12)
    head.next = head
    head.prev = head
    print(dlist_to_str(head))

    # case 3 - fine
    head = DListNode(12)
    node_1 = DListNode(10)
    head.next = node_1
    node_1.prev = head
    print(dlist_to_str(head))

test_dlist_to_str()

'list insert things'

def test_sorted_list_insert():
    # return other
    print(sorted_list_insert(None, 'none'))

    # tuple thing
    one = ListNode((None, 10))
    two = ListNode((None, 20))
    print(sorted_list_insert(two, one).val)

    # same tuple?
    one = ListNode((10, 20))
    two = ListNode((20, 20))
    print(sorted_list_insert(two, one).val)

    # third bit???
    one = ListNode((10, 20))
    one.next = ListNode((10, 50))
    two = ListNode((20, 30))
    print(sorted_list_insert(one, two).val)

    one = ListNode((10, 20))
    one.next = ListNode((30, 30))
    two = ListNode((20, 30))
    print(sorted_list_insert(one, two).val)

    one = ListNode((10, 20))
    one.next = ListNode((10, 30))
    two = ListNode((20, 30))
    print(sorted_list_insert(one, two).val)

test_sorted_list_insert()


def print_list_test():
    # head is none
    head = None
    print_list(head)

    # cur is not none
    head = ListNode((10, 20))
    head.next = ListNode((20, 30))
    head.next.next = ListNode((30, 40))
    print_list(head)

print_list_test()