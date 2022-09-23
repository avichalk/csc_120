from list_node import ListNode

def too_many_aliases():
    ''
    arr1 = [11, 22]
    arr2 = [33, 44]
    a = [arr1, arr2]
    b = [arr1, arr2]
    one = [a, b, a, b]
    return one