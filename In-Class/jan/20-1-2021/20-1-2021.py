#Part 1
def new_func(string, integer):
    new_string=''
    for i in range(integer+1):
        new_string+=string
    return new_string

#Part 2
input_1 = int(input())
input_2 = int(input())
while input_1<=input_2:
    print(input_1)
    input_1+=1

#Part 3
import random
total = 0
while True:
    i = random.randint(1,20)
    if i == 20:
        total+=40
    elif i == 1:
        print(total)
        break
    else:
        total+=i

#Part 4
'''
It adds each individual character of the string into a
list.
'''
def string_converter():
    string = 'supercalifragalisticexpialidocious'
    i=0
    my_list=[]
    while i<len(string):
        my_list.append(string[i])
        i+=1
    return my_list

#Part 5
def string_func(string):
    my_dic={}
    i=0
    while i<len(string):
        my_dic[string[i]]=0
        i+=1
    for i in string:
        my_dic[i]+=1
    if 'a' in string:
        print(my_dic['a'])
    else:
        print(0)

'''
Word of the day: gamedev
'''