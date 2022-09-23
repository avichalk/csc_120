
# Part 1
file_open = open('data.txt', 'r')
with file_open as file:
    for i in file:
        i = i.strip('\n')
        print(i)
file_open.close()

## There is a blank space because print adds an extra newline character.
## We can solve this by removing the newline.
## You open data.txt as a file in read mode, iterate through each line,
## and strip the newline from each line before printing it.

# Part 2
file_obj = open('output.txt', 'w')
file_obj.write('Do i actually see')
file_obj.write('\nwith my own very eyes, a man whos not heard')
file_obj.write('\na jelical cat?')
file_obj.close()

#Part 3
def dic_search(my_dic):
    maxim = 0
    max_2 = ''
    max_key = ''
    for i in my_dic:
        if my_dic[i]>maxim:
            max_2 = max_key
            max_key = i
            maxim = my_dic[i]
    return max_key, max_2

#Part 3
def dic_search(my_dic):
    maxim = 0
    neg_val = 0
    max_2 = ''
    max_key = ''
    for i in my_dic:
    if my_dic[i]>maxim:
        max_2 = max_key
        max_key = i
        maxim = my_dic[i]
    return max_key, max_2

## Word of the Day: Foobazbar