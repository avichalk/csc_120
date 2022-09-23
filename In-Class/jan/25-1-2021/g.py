Activity 1
# Ques 1
A reference refers to something that can be used
as a pointer to a certain object. The variable x
does not contain the array, it just refers to the
array.

# Ques 2
Step 1 - Storing the list in memory
Step 2 - Variable x created to point to that point in memory.

# Ques 3
Array elements are stored at different points in memory,
so you dont have to access the entire array to get one element.

Activity 4
# y isn't gone, it's just floating around in memory. However,
# it's considered junk data so if the memory it occupies has
# to be used by something else, it just gets overwritten.

Activity 5
# id returns the memory address of the object, which changes
# all the time. If two functions have different ids, they are
# pointing at different objects in memory. If two functions
# have the same id, it is the same object.