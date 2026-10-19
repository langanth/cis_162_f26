
"""
Given an array of ints, return True if 6 appears either
as the first or last element of a list. The array will be length 1 or more

first_last6([1, 3, 6]) -> True
first_last6([6, 1, 2, 3]) -> True
first_last6([13, 6, 1, 2, 3]) -> False

"""

def first_last6(lst):
    # first = lst[0]
    # last = lst[-1]
    if lst[0] == 6:
        return True
    if lst[-1] == 6:
        return True
    return False

    # return lst[0] == 6 or lst[-1] == 6

"""
Given two arrays, determine if they both have the same last element.
Assume the lists will be a length of 1 or more.

common_end([1, 3, 5], [3, 4, 5]) -> True
common_end([1, 2, 3], [7, 3, 2]) -> False
common_end([1, 2, 3], [1, 3]) -> True

"""

def common_end(a, b):
    return a[-1] == b[-1]

"""
Given 2 int lists, a and b, each length 3, return a new array length
of 2 containing middle elements.

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

"""

def middle_way(a, b):
    lst = []
    lst.append(a[1])
    lst.append(b[1])
    # lst.extend([a[1], b[1]])
    return lst
    # return [a[1], b[1]]

"""
Return the number of evens in the given array.
All values are assumed to be integers. 

count_even([2, 1, 2, 3, 4]) -> 3
count_evens([2, 2, 0]) -> 
count_evens([1,3, 5]) -> 0

"""

def count_evens(lst):
    total = 0
    for i in lst:
        if i % 2 == 0:
            total += 1
    return total


ui = int(input('Please enter an integer you wish find: '))
lst = [2, 4, 6]
print(lst.index(ui))

for i in lst:
    if i == ui:
        print('found it!')

if ui in lst:
    print('True')