while True:
    user_input=input()
    if user_input.strip()=='quit':
        break
    i=0
    blank_no=0
    while i<len(user_input):
        if user_input[i]==' ':
            blank_no+=1
            i+=1
        else:
            break
    print('This line started with', blank_no, 'space characters.')