from random import randint


def find_max(nums):
    mx = nums[0]    
    # for loop to iterate through list
    for i in nums:
        if mx < i:
            mx = i
    return mx

def calc_average(nums):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)

def calc_sum_even(nums):
    total = 0
    for i in nums:
        if i % 2 == 0:
            total += i
    return total

"""
[[1,2,3], [4,5,6]] -> [1,2,3,4,5,6]
"""
def flatten_list(lst):
    new_lst = []

    for row in lst:
        for col in row:
            new_lst.append(col)

    """
    for row in range(len(lst)):
        for col in range(len(lst[row]))
            new_lst.append(lst[row][col])
    """

    return new_lst

lst = [[1,2,3], [4,5,6]]
lst2 = [[1,2,3], [4], [5, 6]]
random_nums = [[randint(1,10) for _ in range(randint(1,5))] for _ in range(randint(3, 10))]

print(flatten_list(lst))
print(flatten_list(lst2))

for i in random_nums:
    print(i)
print(flatten_list(random_nums))