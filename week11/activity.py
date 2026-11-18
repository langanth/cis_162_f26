# Loop 1

"""i = 0
while i < 10:
    print(i)
    # not a part of original loop
    i += 1 # Will cause it to loop 10 times

number = 2

while number < 10:
    print(number)
    number += 2

print(number)"""


def random_sort_function(lst):
    new_lst = []
    mx = lst[0]
    for i in lst:
        if i >= mx:
            new_lst.append(i)
            mx = i
    return new_lst

def counting(val, flr):

    while val > flr:
        print(val)
        val = val // 2
    


if __name__ == "__main__":
    '''lst = [1, 2, 3, 4, 5]
    print(random_sort_function(lst))
    counting(20, 2)
    lst = [['a', 'z'], ['b', 'y']]
    print(type(lst[0][1]))
    for i in range(0, 100):
        y = i % 10
        print(y)'''

    flag = True

    while flag:
        print(flag)
        flag = False

    i = 0
    while i < 100:
        print(i)
        if i > 10:
            break
        if i < 10:
            i = 0
        i += 1

