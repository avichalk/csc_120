# word of the day: none

# Activity 1
cur = head
while cur is not None:
    cur = cur.next()

# Activity 2
# if head is none, cur will immediately go to none,
# and therefore the while loop doesn't iterate.

# Activity 3
cur = head
x=1
while cur is not None:
    if x % 2 == 0:
        print(cur)
    cur = cur.next()
    x+=1

# Activity 4
cur = head
while cur is not None:
    cur = cur.next()
    if cur.next() is not None:
        cur = cur.next()
# if you try to read the next field of a none object,
# python will throw a nonetype error.