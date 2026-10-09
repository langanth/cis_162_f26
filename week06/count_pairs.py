
"""
Given a string, return a new string where
every letter has been doubled.

Example:
    "The" --> "TThhee"
"""
def manual_double_letter(st):
    dst = ''
    dst += st[0] + st[0]
    dst += st[1] + st[1]
    dst += st[2] + st[2]
    return dst

def double_letter(st):
    dst = ''
    x = 0
    while x < len(st):
        dst += st[x] * 2
        x += 1
    return dst

def count_pairs(st):
    c = 0
    i = 0
    # i = 1
    while i + 1 < len(st):
    #while i < len(st) - 1:
    #while i < len(st):
        if st[i] == st[i + 1]:
            c += 1
        i += 1
    return c

""""
return the number of times that the string
code appears anywhere in the given string,
except we'll accept any letter for the 'd'.
cope, cooe, cole, coke, come, cone

'aaacodebbb' --> 1
'codexxcode' --> 2
'cozexcooe' --> 2
"""
def count_code(st):
    c = 0
    i = 0
    end_point = len(st) - 3
    while i < end_point:
        if st[0] == 'c' and st[1] == 'o' and st[3] == 'e':
            c += 1
        i += 1
    return c


def retake(m1, retake):
    return (m1* .15) + (retake * .85)

if __name__ =="__main__":
    #print(retake(82, 85))
    #print(double_letter('abc'))
    print(count_pairs('xxxyxyxxy'))