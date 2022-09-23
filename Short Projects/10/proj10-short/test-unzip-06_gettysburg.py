#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



# --- GETTYSBURG ADDRESS ---

gettysburg_raw = """four score and seven years ago our fathers brought forth on this continent a
new nation, conceived in liberty, and dedicated to the proposition that all men
are created equal.

now we are engaged in a great civil war, testing whether that nation, or any
nation so conceived and so dedicated, can long endure. we are met on a great
battlefield of that war. we have come to dedicate a portion of that field, as a
final resting place for those who here gave their lives that that nation might
live. it is altogether fitting and proper that we should do this.

but, in a larger sense, we can not dedicate, we can not consecrate, we can not
hallow this ground. the brave men, living and dead, who struggled here, have
consecrated it, far above our poor power to add or detract. the world will
little note, nor long remember what we say here, but it can never forget what
they did here. it is for us the living, rather, to be dedicated here to the
unfinished work which they who fought here have thus far so nobly advanced. it
is rather for us to be here dedicated to the great task remaining before
us-that from these honored dead we take increased devotion to that cause for
which they gave the last full measure of devotion-that we here highly resolve
that these dead shall not have died in vain-that this nation, under god, shall
have a new birth of freedom-and that government of the people, by the people,
for the people, shall not perish from the earth."""



# --- COMPRESSED FORM ---
#
# I wrote a VERY DUMB compressor function, which I used to compress the Gettysbug
# Address.  I'm sure that the compression rate is *far* below what a good
# function would generate, but hey, it's still fun!
#
# And yes, this line is long.  The longest.  Long beyond all measure.  Long.
# Live with it.


gettysburg_comp = ['f', 'o', 'u', 'r', ' ', 's', 'c', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 's', 'e', 'v', 'e', 'n', ' ', 'y', 'e', 'a', 'r', 's', ' ', 'a', 'g', 'o', ' ', (30, 4), 'f', 'a', 't', 'h', 'e', 'r', 's', ' ', 'b', 'r', 'o', 'u', 'g', 'h', 't', ' ', 'f', 'o', 'r', 't', 'h', ' ', 'o', 'n', ' ', 't', 'h', 'i', 's', ' ', 'c', 'o', 'n', 't', 'i', 'n', 'e', 'n', 't', ' ', 'a', '\n', 'n', 'e', 'w', ' ', 'n', 'a', 't', 'i', 'o', 'n', ',', (24, 4), 'c', 'e', 'i', 'v', 'e', 'd', ' ', 'i', 'n', ' ', 'l', 'i', 'b', 'e', 'r', 't', 'y', ',', (100, 5), 'd', 'e', 'd', 'i', 'c', 'a', 't', 'e', 'd', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'p', 'r', 'o', 'p', 'o', 's', 'i', 't', 'i', (84, 5), 'a', 't', ' ', 'a', 'l', 'l', ' ', 'm', 'e', 'n', '\n', 'a', 'r', 'e', ' ', 'c', 'r', 'e', (44, 5), 'e', 'q', 'u', 'a', 'l', '.', '\n', '\n', 'n', 'o', 'w', ' ', 'w', 'e', ' ', 'a', 'r', 'e', ' ', 'e', 'n', 'g', 'a', 'g', (97, 6), 'a', ' ', 'g', 'r', 'e', 'a', 't', ' ', 'c', 'i', 'v', 'i', 'l', ' ', 'w', 'a', 'r', ',', ' ', 't', 'e', 's', 't', 'i', 'n', 'g', ' ', 'w', 'h', 'e', 't', 'h', 'e', 'r', ' ', 't', 'h', 'a', 't', (158, 9), 'o', 'r', ' ', 'a', 'n', 'y', '\n', 'n', 'a', 't', 'i', 'o', 'n', ' ', 's', 'o', (175, 11), 'a', 'n', 'd', ' ', 's', 'o', ' ', 'd', 'e', 'd', 'i', 'c', 'a', 't', 'e', 'd', ',', ' ', 'c', 'a', 'n', ' ', 'l', 'o', 'n', 'g', ' ', 'e', 'n', 'd', 'u', 'r', 'e', '.', ' ', 'w', 'e', ' ', 'a', 'r', 'e', ' ', 'm', 'e', 't', ' ', 'o', 'n', ' ', 'a', ' ', 'g', 'r', 'e', 'a', 't', '\n', 'b', 'a', 't', 't', 'l', 'e', 'f', 'i', 'e', 'l', 'd', ' ', 'o', 'f', ' ', 't', 'h', 'a', 't', ' ', 'w', 'a', 'r', (47, 5), 'h', 'a', 'v', 'e', ' ', 'c', 'o', 'm', 'e', ' ', 't', (91, 10), ' ', 'a', ' ', 'p', 'o', 'r', 't', 'i', 'o', 'n', ' ', 'o', 'f', ' ', 't', 'h', 'a', 't', ' ', 'f', 'i', 'e', 'l', 'd', ',', ' ', 'a', 's', ' ', 'a', '\n', 'f', 'i', 'n', 'a', 'l', ' ', 'r', 'e', 's', 't', 'i', 'n', 'g', ' ', 'p', 'l', 'a', 'c', 'e', ' ', 'f', 'o', 'r', (41, 3), 'o', 's', 'e', ' ', 'w', 'h', 'o', ' ', 'h', 'e', 'r', 'e', ' ', 'g', 'a', 'v', 'e', (20, 3), 'e', 'i', 'r', ' ', 'l', 'i', 'v', 'e', 's', (73, 5), (238, 12), ' ', 'm', 'i', 'g', 'h', 't', '\n', 'l', 'i', 'v', 'e', '.', ' ', 'i', 't', ' ', 'i', 's', ' ', 'a', 'l', 't', 'o', 'g', 'e', 't', 'h', 'e', 'r', ' ', 'f', 'i', 't', 't', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'p', 'r', 'o', 'p', (19, 3), 't', 'h', 'a', 't', ' ', 'w', 'e', ' ', 's', 'h', 'o', 'u', 'l', 'd', ' ', 'd', 'o', (18, 3), 'i', 's', '.', '\n', '\n', 'b', 'u', 't', ',', ' ', 'i', 'n', ' ', 'a', ' ', 'l', 'a', 'r', 'g', 'e', 'r', ' ', 's', 'e', 'n', 's', 'e', ',', (44, 4), 'c', 'a', 'n', ' ', 'n', 'o', 't', ' ', 'd', 'e', 'd', 'i', 'c', 'a', 't', (21, 14), 'c', 'o', 'n', 's', 'e', 'c', 'r', (23, 15), '\n', 'h', 'a', 'l', 'l', 'o', 'w', ' ', 't', 'h', 'i', 's', ' ', 'g', 'r', 'o', 'u', 'n', 'd', '.', (13, 3), 'e', ' ', 'b', 'r', 'a', 'v', 'e', ' ', 'm', 'e', 'n', ',', ' ', 'l', 'i', 'v', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'd', 'e', 'a', 'd', ',', ' ', 'w', 'h', 'o', ' ', 's', 't', 'r', 'u', 'g', 'g', 'l', 'e', 'd', ' ', 'h', 'e', 'r', 'e', ',', ' ', 'h', (47, 3), '\n', 'c', 'o', 'n', 's', 'e', 'c', 'r', 'a', 't', (23, 3), 'i', 't', ',', ' ', 'f', 'a', 'r', ' ', 'a', 'b', 'o', 'v', 'e', ' ', 'o', 'u', 'r', ' ', 'p', 'o', 'o', (5, 4), 'w', 'e', 'r', ' ', 't', 'o', ' ', 'a', 'd', 'd', ' ', 'o', 'r', ' ', 'd', 'e', 't', 'r', 'a', 'c', 't', (117, 6), 'w', 'o', 'r', 'l', 'd', ' ', 'w', 'i', 'l', 'l', '\n', 'l', 'i', 't', 't', 'l', 'e', ' ', 'n', 'o', 't', 'e', ',', (6, 3), 'r', ' ', 'l', 'o', 'n', 'g', ' ', 'r', 'e', 'm', 'e', 'm', 'b', 'e', 'r', ' ', 'w', 'h', 'a', 't', ' ', 'w', 'e', ' ', 's', 'a', 'y', (129, 7), 'b', 'u', 't', ' ', 'i', 't', ' ', 'c', 'a', 'n', ' ', 'n', 'e', 'v', 'e', 'r', ' ', 'f', 'o', 'r', 'g', 'e', 't', ' ', 'w', 'h', 'a', 't', '\n', 't', 'h', 'e', 'y', ' ', 'd', 'i', 'd', ' ', 'h', 'e', 'r', 'e', '.', (40, 4), 'i', 's', (33, 4), ' ', 'u', 's', ' ', 't', 'h', 'e', ' ', 'l', 'i', 'v', 'i', 'n', 'g', ',', ' ', 'r', 'a', (14, 3), 'r', ',', ' ', 't', 'o', ' ', 'b', 'e', ' ', 'd', 'e', 'd', 'i', 'c', 'a', 't', 'e', (55, 6), ' ', 't', 'o', ' ', 't', 'h', 'e', '\n', 'u', 'n', 'f', 'i', 'n', 'i', 's', 'h', 'e', 'd', ' ', 'w', 'o', 'r', 'k', ' ', 'w', 'h', 'i', 'c', 'h', (26, 4), 'y', ' ', 'w', 'h', 'o', ' ', 'f', 'o', 'u', 'g', 'h', 't', (50, 6), 'h', 'a', 'v', 'e', ' ', 't', 'h', 'u', 's', ' ', 'f', 'a', 'r', ' ', 's', 'o', ' ', 'n', 'o', 'b', 'l', 'y', ' ', 'a', 'd', 'v', 'a', 'n', 'c', 'e', 'd', '.', ' ', 'i', 't', '\n', 'i', 's', (118, 7), (144, 9), 'o', ' ', 'b', 'e', ' ', 'h', 'e', 'r', 'e', (934, 18), 'g', 'r', 'e', 'a', 't', ' ', 't', 'a', 's', 'k', ' ', 'r', 'e', 'm', 'a', 'i', 'n', 'i', 'n', 'g', ' ', 'b', 'e', 'f', 'o', 'r', 'e', '\n', 'u', 's', '-', 't', 'h', (30, 3), 'f', 'r', 'o', 'm', ' ', 't', 'h', 'e', 's', 'e', ' ', 'h', 'o', 'n', (26, 3), 'd', ' ', 'd', 'e', 'a', 'd', ' ', 'w', 'e', ' ', 't', 'a', 'k', 'e', ' ', 'i', 'n', 'c', 'r', 'e', 'a', 's', (23, 5), 'v', 'o', 't', 'i', 'o', 'n', ' ', 't', 'o', ' ', 't', 'h', 'a', 't', ' ', 'c', 'a', 'u', 's', 'e', ' ', 'f', 'o', 'r', '\n', 'w', 'h', 'i', 'c', 'h', (21, 3), 'e', 'y', ' ', 'g', 'a', 'v', 'e', (10, 4), ' ', 'l', 'a', 's', 't', ' ', 'f', 'u', 'l', 'l', ' ', 'm', 'e', 'a', 's', 'u', 'r', 'e', ' ', 'o', 'f', (68, 9), '-', 't', 'h', 'a', 't', ' ', 'w', 'e', ' ', 'h', 'e', 'r', (5, 3), 'i', 'g', 'h', 'l', 'y', ' ', 'r', 'e', 's', 'o', 'l', 'v', 'e', '\n', (28, 5), 't', 'h', 'e', 's', 'e', ' ', 'd', 'e', 'a', 'd', ' ', 's', 'h', 'a', 'l', 'l', ' ', 'n', 'o', 't', ' ', 'h', 'a', 'v', (20, 3), 'i', 'e', 'd', ' ', 'i', 'n', ' ', 'v', 'a', 'i', 'n', '-', (44, 7), 'i', 's', ' ', 'n', 'a', 't', 'i', 'o', 'n', ',', ' ', 'u', 'n', 'd', 'e', 'r', ' ', 'g', 'o', 'd', ',', ' ', 's', 'h', 'a', 'l', 'l', '\n', 'h', 'a', 'v', 'e', ' ', 'a', ' ', 'n', 'e', 'w', ' ', 'b', 'i', 'r', 't', 'h', ' ', 'o', 'f', ' ', 'f', 'r', 'e', 'e', 'd', 'o', 'm', '-', 'a', 'n', 'd', ' ', 't', 'h', 'a', 't', (48, 3), 'v', 'e', 'r', 'n', 'm', 'e', 'n', 't', (31, 4), 't', 'h', 'e', ' ', 'p', 'e', 'o', 'p', 'l', 'e', ',', ' ', 'b', 'y', (15, 12), '\n', 'f', 'o', 'r', (31, 13), 's', 'h', 'a', 'l', 'l', ' ', 'n', 'o', 't', ' ', 'p', 'e', 'r', 'i', 's', 'h', ' ', 'f', 'r', 'o', 'm', ' ', 't', 'h', 'e', ' ', 'e', 'a', 'r', 't', 'h', '.']

one_test(gettysburg_comp)



print()
print("TESTCASE COMPLETED")


