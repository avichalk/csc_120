#! /usr/bin/python3

from proj06_linked_list_funcs import *
from list_node                import *


head                          = ListNode(5)
head.next                     = ListNode(4)
head.next.next                = ListNode(3)
head.next.next.next           = ListNode(2)
head.next.next.next.next      = ListNode(1)
head.next.next.next.next.next = ListNode(0)



print(f"Original list: {head}")

print("--- calling print_rev() ---")
print_rev(head)
print("--- print_rev() completed ---")

print()
print("TESTCASE COMPLETED")

