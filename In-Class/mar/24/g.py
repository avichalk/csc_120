# WOTD: Debug Covid

# Activity 1
data = []
while True:
    val = input("Enter a number (blank line to end)")
    if val == "":
        break
    data.append(int(val))

for v in sorted(data):
    print(v)

# It prints numbers out of order because you're inputting a string, and it sorts by length.
# we fix this by making it an int.

# Activity 2
def log10(val):
    val = float(val)
    count = 0
    while  val >= 10:
        val = val // 10
        count += 1
    return count

# x = log10(20)
# print(x)

# it fails because sometimes dividing a number by 10
# reduces it to 0. We can fix this by making it while val >= 10

import random
def test_log10():
    for i in range(100):
        v = random.randint(1, 1000*1000)
        actual   = log10(v)
        expected = len(str(v))
        if actual != expected:
            print(f"BUG: log10({v}):   actual={actual} expected={expected}")
#test_log10()

# Activity 2
# The bug appears to be that it counts one extra for the expected.
# log(100) is 2, but the test counts it as 3 because it takes the length
# which includes the 1 at the front.

import random
def test_log10():
    for i in range(100):
        v = random.randint(1, 1000*1000)
        actual   = log10(v)
        expected = len(str(v)) - 1
        if actual != expected:
            print(f"BUG: log10({v}):   actual={actual} expected={expected}")
test_log10()