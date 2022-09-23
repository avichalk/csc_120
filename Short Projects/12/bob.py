def main():
    try:
        filename = input()
        file = open(filename, 'r')
    except:
        print(f'ERROR: Could not open the input file: {filename}')
        return

    words = get_file_data(file)

    inpt = input()

    if inpt == 'dump':
        dump_it(words)
    else:
        pals(words, inpt)

def pals(words, inpt):

    print('1-WORD PALINDROMES:')
    simple_pal_set = set()

    for i in words:
        if simple_pal(i):
            simple_pal_set.add(i)

    for i in sorted(simple_pal_set):
        print(f'  {i}')
    print()

    print('2-WORD AND 3-WORD PALINDROMES:')
    two_and_three_pal(words)
    print()

    big_ol_pals(words, int(inpt))

def simple_pal(word):
    if len(word) < 2:
        return True

    if word[0] != word[-1]:
        return False

    return simple_pal(word[1:-1])

def two_and_three_pal(words):
    pals = set()
    for i in words:
        for j in words:
            if simple_pal(i+j):
                pals.add(i+j)
            for k in words:
                if simple_pal(i+j+k):
                    pals.add(i+j+k)

    for i in sorted(pals):
        print(f'  {i}')


def big_ol_pals(words, n):
    ''
    all_words = init_and_add_to_set(words)
    yes_pals = {}

    for i in range(1, n+1):
        if i in all_words:
            for j in all_words[i]:
                if simple_pal(j):
                    if len(j) not in yes_pals:
                        yes_pals[len(j)] = set()
                    yes_pals[len(j)].add(j)
                else:
                    for k in words:
                        if not simple_pal(k):
                            if len(j+k) not in all_words:
                                all_words[len(j+k)] = set()
                            all_words[len(j+k)].add(j+k)

    for i in range(1, n+1):
        if i in all_words:
            print(f'PALINDROMES OF LENGTH {i}    - length of candidate list: {len(all_words[i])}')
            if i in yes_pals:
                for j in sorted(yes_pals[i]):
                    print(f'  {j}')
        else:
            print(f'PALINDROMES OF LENGTH {i}    - length of candidate list: 0')
        print()

def init_and_add_to_set(array):
    data = {}
    for i in array:
        if len(i) not in data:
            data[len(i)] = set()
        data[len(i)].add(i)
    return data

def dump_it(words):
    print('WORD LIST:')
    for i in sorted(words):
        print(f'  {i}')

def get_file_data(file):
    words = set()
    for i in file.readlines():
        i = [i.strip() for i in i.split(' ') if i]
        for j in i:
            j = "".join(i for i in j if i.isalpha())
            j = j.strip()
            if len(j) > 1:
                words.add(j.lower())

    return sorted(words)

if __name__ == '__main__':
    main()