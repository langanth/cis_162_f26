


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

lst = [1, 2, 3 ,4]
print(calc_sum_even(lst))