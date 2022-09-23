# WOTD: wrapper

import random
# Activity 1
def sumlist_sliceHalf(vals):
    if len(vals) == 0:
        return 0
    if len(vals) == 1:
        return vals[0]
    mid = len(vals) // 2
    return sumlist_sliceHalf(vals[:mid ]) + \
    sumlist_sliceHalf(vals[ mid:])

def gen_rand(n):
    array = []
    print('starting array')
    for i in range(n):
        array.append(random.randint(0, 100))
    print('array is done')
    return array

#print(sumlist_sliceHalf(gen_rand(1000000)))
# it does appear to run in O(nlogn)

# Activity 2
def sumlist_pretend_sliceHalf(vals):
    return _sumlist_pretend_sliceHalf(vals, 0,len(vals))
def _sumlist_pretend_sliceHalf(vals, start,end):
    if len(vals[start:end]) == 0:
        return 0
    if len(vals[start:end]) == 1:
        return vals[0]
    return _sumlist_pretend_sliceHalf(vals, start+1, int(len(vals)/2)-1) + \
    _sumlist_pretend_sliceHalf(vals, int(len(vals)/2)-1, len(vals)-1)

# Activity 3
# print(sumlist_pretend_sliceHalf(gen_rand(100)))
# a lot faster than the one that actually slices

# Activity 4
def bin_ser(array, val):
    return _bin_search(array, val, 0, len(array))

def _bin_search(array, val, start, end):
    if len(array[start:end] == 0:
        return 'not found'
    if len(array[start:end]) == 1:
        if array[start:end] == val:
            return 'found'
        return 'not found'
    if array[int(end/2)] > val:
        return _bin_search(array, val, int(end/2), end)
    return _bin_search(array, val, start, int(end/2)+1)

