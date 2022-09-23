from time import time
import random

# Activity 1
# We think they both run in O(n) time. We can check this.
def count_dups_1(data):
    so_far = []
    count  = 0
    for val in data:
        if val in so_far:
            count += 1
        else:
            so_far.append(val)
    return count

def count_dups_2(data):
    so_far = set()
    count  = 0
    for val in data:
        if val in so_far:
            count += 1
        else:
            so_far.add(val)
    return count

def genRandArr(num):
    arr = []
    for i in range(num):
        arr.append(i)
    return arr

# arr = genRandArr(10000)
# start = time()
# count_dups_1(arr)
# print(f'{time()-start}')
# start = time()
# count_dups_2(arr)
# print(f'{time()-start}')

# we find that it takes much longer when it is an array.

# Activity 2
# The runtime of this function would be n^2 at the least, and maybe n^3.
# Once the dataset is sufficiently small, it is essentially O(1)
# yes, because for each element in data1 each element in data2 is also called.

# Activity 3
def genRandDic(num):
    dic = {}
    for i in range(num):
        dic[i] = random.randint(0, num)
    return arr
# we think this function runs in O(n^2) time
def lookup_in_dict(dic, search):
    retval = []
    for s in search:
        found = None
        for key in dic:
            if dic[key] == s:
                found = key
                break
        retval.append(found)
    return retval
arr = genRandArr(1000)
dic = genRandDic(1000)
start = time()
lookup_in_dict(dic, arr)
print(f'{time()-start}')
arr = genRandArr(10000)
dic = genRandDic(10000)
start = time()
lookup_in_dict(dic, arr)
print(f'{time()-start}')
# increasing n by an order of 10 increases the time taken by 100. looks like we were right.

# Word of the day- NONE