#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



data = list('This song ') + [(8, 3)] + list('just six words l') + [(23, 3)] + ['\n'] + \
       [(33, 99)] + list("Couldn't think of any lyrics\n") + \
       list('No I never wrote') + [(37, 3)] + ['e'] + [(28, 8)] + ['S'] + [(28, 3)] + list("'ll") + [(85, 8)] + list('ng') + [(57, 5)] + list('old') + [(33, 8)] + list('That com') + [(54, 3)] + list('o mind, child\n') + \
       list('You really') + [(92, 3)] + list('ed') + [(142, 6)] + ['\n'] + \
       list('Whole') + [(148, 3)] + list('tta rhym') + [(82, 3)] + [(26, 7)] + [(48, 4)] + ['g'] + [(24, 9)] + list('e s') + [(79, 3)] + [(108, 3)] + [(30, 6)] + list(', mm-mm\n') + \
       list('To do it, t') + [(10, 27)] + [(39, 19)] + list(' right') + [(156, 8)] + [(403, 132)] + list('I know t') + [(320, 4)] + list("you're probably") + [(56, 3)] + list('re\n') + \
       list("'Cause") + [(411, 3)] + list('di') + [(443, 5)] + list('write') + [(383, 5)] + ['m'] + [(31, 4)] + ['I'] + [(86, 5)] + [(29, 8)] + list('get') + [(236, 3)] + [(393, 4)] + list('plete') + [(261, 4)] + list('So') + [(93, 5)] + list("'s why I") + [(349, 8)] + list('epeat') + [(32, 3)] + [(162, 33)] + list(' (') + [(16, 14)] + [')'] + [(50, 51)] + list('Oh I') + [(455, 3)] + ['k'] + [(184, 3)] + [(501, 7)] + list('money') + [(74, 3)] + list('ey pa') + [(203, 3)] + [(26, 4)] + list('ton') + [(659, 3)] + [(27, 11)] + [(269, 5)] + list("ayin'") + [(33, 4)] + [(210, 3)] + list('nty') + [(34, 11)] + ['o'] + [(650, 6)] + ['t'] + [(143, 8)] + [(471, 8)] + [(228, 8)] + list('fi') + [(690, 3)] + list('time') + [(77, 3)] + list('ree') + [(663, 4)] + list('utes') + [(154, 4)] + list('th') + [(72, 3)] + [(28, 6)] + list('Oh, h') + [(386, 3)] + ['w'] + [(46, 4)] + ['I'] + [(53, 6)] + [(629, 4)] + list('uch') + [(33, 5)] + [(628, 8)] + [(768, 5)] + list('thr') + [(43, 3)] + list('in a') + [(36, 3)] + list('lo,') + [(8, 15)] + ['\n'] + \
       ['A'] + [(15, 13)] + list(' here') + [(614, 133)] + [(33, 9)] + list("'s") + [(285, 4)] + list(' no') + [(1026, 4)] + ["'"] + [(556, 4)] + list('say\n') + \
       list('But') + [(992, 3)] + ['m'] + [(534, 3)] + ['c'] + [(52, 3)] + ['i'] + [(72, 4)] + ['t'] + [(611, 4)] + list('way') + [(673, 8)] + list('if') + [(285, 3)] + ['p'] + [(40, 3)] + list('my') + [(992, 5)] + list(' t') + [(848, 4)] + [(30, 8)] + list('I c') + [(1115, 4)] + list(' f') + [(26, 4)] + ['a'] + [(99, 3)] + list('od') + [(960, 7)] + [(259, 3)] + [(356, 6)] + ['y'] + [(985, 9)] + list('have-a') + [(354, 3)] + list('sic') + [(1008, 4)] + [(1049, 5)] + [(1061, 8)] + list('catchy') + [(29, 6)] + [(216, 11)] + list('ha') + [(185, 5)] + [(517, 12)] + [(34, 5)] + [(186, 3)] + [(241, 15)] + [(518, 8)] + ['A'] + [(138, 3)] + ['s'] + [(1207, 7)] + [(552, 4)] + list("' em o") + [(1246, 3)] + [(26, 4)] + [(9, 5)] + list(' a') + [(9, 11)] + [(27, 32)] + [(519, 7)] + [(61, 54)] + list(' again\n') + \
       ['S'] + [(405, 13)] + [','] + [(421, 15)] + [(31, 32)] + ['\n']

one_test(data)



print()
print("TESTCASE COMPLETED")

