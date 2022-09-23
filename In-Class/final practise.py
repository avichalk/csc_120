def count_occur(num1, num2):
    ''
    count = 0
    num2 = str(num2)
    num1 = str(num1)
    i = 0
    z = 1
    while i < len(num1):
        if i+len(num2) <= len(num1):
            if num1[i:i+len(num2)] == num2:
                count += 1
                i += len(num2)
            else:
                i += 1
                z = 1
        else:
            if z == 1:
                z = 0
            else:
                i += 1
    return count

def traverse_tree(root):
    cur = root
    while cur is not None:
        print(cur.val)
        cur = cur.left
    cur = root
    while cur is not None:
        cur = cur.right
        print(cur.val)

def most_word(filename):
    file = open(filename, r)
    filines = file.readlines()
    fi = []
    for i in filines:
        fi.append(i.strip())
    word_dic = {}
    for i in filines:
        if i in word_dic:
            word_dic[i] += 1
        else:
            word_dic[i] = 1
    maxim = 0
    word = ''
    for i in sorted(word_dic):
        if word_dic[i] > maxim:
            maxim = word_dic[i]
            word = i
    return word

def find_min_and_max(head):
    if head is None:
        print('emptylol')
        return
    cur = head
    arr = []
    while cur is not None:
        arr.append(cur.val)
        cur = cur.next
    print(max(arr))
    print(min(arr))

def find_max_key(dic):
    maxim = 0
    key = ''
    for i in dic:
        if i > maxim:
            maxim = i
            key = dic[i]
    return key

def double_items(items):
    i = 0
    while i < len(items):
        items.insert(i, items[i])
        i += 2
    print(items)

def sum_list(head):
    su = 0
    while head is not None:
        su += head.val
        head = head.next
    return su

def del_every_other(head):
    cur = head
    while cur is not None:
        new = cur.next.next
        cur.next = new
        cur = cur.next

def remove_odd(head):
    cur = head
    while cur is not None:
        if cur.next.val % 2 != 0:
            cur.next = cur.next.next
        cur = cur.next
    return head

def find_mid(head):
    cur = head
    count = 1
    while cur is not None:
        count += 1
        cur = cur.next
    while count > 0:
        head = head.next
    head.next = None
    return head

def tree_swap_vals(root):
    if root is None:
        return
    if root.right is not None and root.left is not None:
        x = root.left.val
        root.left.val = root.right.val
        root.right.val = x
    tree_swap_vals(root.left)
    tree_swap_vals(root.right)
    return root

def remove_odd(head):
    if head is None:
        return
    if head.next is not None:
        if head.next.val % 2 != 0:
            head.next = head.next.next
            remove_odd(head.next)

def sum_range_bst(root, low, high):
    if root is None:
        return 0
    if low < root.val < high:
        return root.val + sum_range_bst(root.left, low, high) + sum_range_bst(root.right, low, high)
    return sum_range_bst(root.left, low, high) + sum_range_bst(root.right, low, high)

def sum_odds(ints):
    if len(ints) == 0:
        return 0
    if ints[0] % 2 != 1:
        return ints[0] + sum_odds(ints[1:])
    return sum_odds(ints[1:])

def count_branches(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + count_branches(root.left) + count_branches(root.right)

def remove_cons(word):
    new = word[0]
    char = word[0]
    for i in word:
        if i != char:
            char = i
            new += i
    return new

def string_rec(word):
    if len(word) == 0:
        return 0
    if word[0].lower() in 'xyz':
        return 1 + string_rec(word[1:])
    return string_rec(word[1:])

def pal_check(word):
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        return pal_check(word[1:-1])
    return False


