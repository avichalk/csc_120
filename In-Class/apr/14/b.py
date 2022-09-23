# Activity 1

import c as nom
def main():
    print('run')

main()

# Both main functions across both files ran.
# that includes the one in the library.

# Activity 2


if __name__ == '__main__':
    main()

# Now only the main from this file runs.

# Activity 3
print(__name__)

# In the case of the imported library, __name__ is the
# name of the file without the extension. In our program
# that is running the code, it is __main__
if __name__ == '__main__':
    nom.main()

#WOTD: testcase