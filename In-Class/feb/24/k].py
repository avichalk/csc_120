# activty one
def count_coins(cup):
    if cup == []:
        return 0
    return cup[0] + count_coins(cup[1:])

# activity two
def last_element(head):
    if head.next is None:
        return head
    return last_element(head.next)

# activity three
def odd_values(array):
    if array == []:
        return 0
    elif array[0] % 2 == 1:
        x = 1
    return x + odd_values(array[1:])

# activity four
def search_linked_list(head, k):
    while head is not None:
        if head.val == k:
            x = True
    return x and search_linked_list(head.next, k)

# (compound) word of the day: stack frame