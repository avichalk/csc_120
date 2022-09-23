def two_lines():
    string_1=str(input())
    string_2=str(input())
    string_1_split=string_1.split()
    string_2_split=string_2.split()
    print('The first line was:', string_1_split)
    print('The second line was:', string_2_split)
    print('')
    string_split=string_1_split + string_2_split
    print('The combination of both lines had', len(string_split), 'words.')
    print('The combined set of words was:', string_split)
    print('')
    print('After sorting, the words were:', sorted(string_split))

two_lines()