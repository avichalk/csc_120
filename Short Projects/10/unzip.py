def unzip(array):
    length = 0
    string = ''

    for i in array:
        assert type(i) == str or type(i) == tuple

        if type(i) == str:
            assert len(i) == 1
            length += len(i)

        if type(i) == tuple:
            assert len(i) == 2

            for j in i:
                assert type(j) == int
                assert j > 0

            length += i[1]

    for i in array:
        if type(i) == str:
            string += i
        if type(i) == tuple:
            assert i[0] < length
            z = i[1]
            while z > 0:
                x = len(string) - i[0]
                string += string[x]
                z -= 1

    return string