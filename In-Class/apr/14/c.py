def main():
    print('imported')

    # Activity 4
    good_count = 0
    # Activity 5
    try:
        try:
            if foobar_func(10, 20, 30) == 100:
                good_count += 1
        except:
            print('test1 failed')
        try:
            if another(10, 0, 30) == another(10, 20, 30):
                good_count += 1
        except ZeroDivisionError:
            print('div by 0 error')
        except:
            print('test2 failed')
        try:
            if more('lmao') == 0:
                good_count += 1
        except:
            print('test3 failed')
    except:
        print('bad things happened')
    if good_count == 3:
        print('fine')
        return
    print(f'bad. only {good_count}/3 cases passed')

def foobar_func(a, b, c):
    return 100

def another(b, a, c):
    z = b*a*c
    z = z/a
    return z

def more(a):
    z = a-30
    return z

if __name__ == '__main__':
    main()

print(__name__)