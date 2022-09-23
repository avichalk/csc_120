# Activity 1

import random
for i in range(10):
    a = random.randint(1,12)
    b = random.randint(1,12)
    question = "What is "+str(a)+" x "+str(b)+"? "
    answer = input(question)
    if int(answer) == a*b:
        print ('Well done!')
    else:
        print("No.")

# Activity 2
def remove_dups(arr):
    count = len(arr)
    i = 0
    while i < count:
        j = i
        while j < count:
            if j != i:
                if arr[j] == arr[i]:
                    arr.pop(j)
                    count -= 1
                    j -= 1
            j += 1
        i += 1

# Errors: indexerror, check all elements as len of array is reducing, and j==i is a problem.

# Word of the day: Debug