#! /usr/bin/python3

from proj06_linked_list_funcs import *
from list_node                import *


head                = ListNode("abc")
head.next           = ListNode("def")
head.next.next      = ListNode("ghi")
head.next.next.next = ListNode("jkl")



print(f"Original list: {head}")

print("--- calling print_rev() ---")
print_rev(head)
print("--- print_rev() completed ---")

print()
print("TESTCASE COMPLETED")

