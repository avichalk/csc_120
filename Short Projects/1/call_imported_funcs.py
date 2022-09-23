def call_imported_funcs():
    import short1_thing as new_file
    input_1=input()
    print(new_file.foo(input_1))
    input_2=input()
    input_3=input()
    print(new_file.bar(input_1, input_2, input_3))

call_imported_funcs()