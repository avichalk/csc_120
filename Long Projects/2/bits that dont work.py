    stack_list, cur_pos_list, origin_var = stack_proc_for_map(stack, cur_pos)
    print('+-----------+')
    i=0
    while i<11:
        string = ''
        if origin_var == 1:
            if i == 5:
                j=1
                while j<10:
                    if j == 5:
                        string+='+'
                    else:
                        string+=' '
                    j+=1
        if cur_pos_list[1] == i:
            if
            j=1
            while j<10:
                if cur_pos_list[0] == j:
                    string+='+'
                else:
                    string+=' '
                j+=1
        for k in stack_list:
            if k[1] == i:
                j=1
                while j<10:
                    if k[0] == j:
                        if origin_var == 1:
                            ''
                        elif origin_var == 0:
                            string+='*'
                        else:
                            string+=' '
                    j+=1
        print('|', string, '|')
        i+=1
    print('+-----------+')

def stack_proc_for_map(stack, cur_pos):
    stack_list = []
    origin_var = 0
    if stack == [(0,0)]:
        origin_var = 1
    else:
        stack.remove((0,0))
        for i in stack:
            stack_list_list = []
            stack_list_list.append(int(i[0])+5)
            stack_list_list.append(int(i[1])+5)
            stack_list.append(stack_list_list)
    cur_pos_list = []
    cur_pos_list.append(int(cur_pos[0])+5)
    cur_pos_list.append(int(cur_pos[1])+5)
    print(stack, origin_var)
    return stack_list, cur_pos_list, origin_var

def print_origin_function(origin_is_cur_pos):
    '''
    I don't actually know why this is here.
    '''
    string_var = ''
    done_y_pos_var = 0
    if origin_is_cur_pos == 0:
            k = 1
            while k<=11:
                if k == 6:
                    string_var+='*'
                    k+=1
                else:
                    string_var+=' '
                    k+=1
                done_y_pos_var = 6
    elif origin_is_cur_pos == 1:
            k = 1
            while k<=11:
                if k == 6:
                    string_var+='+'
                    k+=1
                else:
                    string_var+=' '
                    k+=1
                done_y_pos_var = 6
    return done_y_pos_var, string_var