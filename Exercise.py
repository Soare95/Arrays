"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums, target):
    val = {}
    my_list = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in val:
            my_list.append(i)
            my_list.append(val[diff])
            return my_list
        val[nums[i]] = i


nums1 = [2, 11, 15, 7]
target = 9

# print(two_sum(nums1, target))

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


def move_zeroes(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums


nums3 = [0, 1, 0, 3, 12]

# print(move_zeroes(nums3))

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every 
element is distinct.
"""


def contains_duplicate(nums):
    has_duplicates = set(nums)
    for i in nums:
        if range(len(has_duplicates)) != range(len(nums)):
            return True
        else:
            return False


nums4 = [1, 2, 3, 4, 3]

# print(contains_duplicate(nums4))

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


def rotate(nums, k):
    i = 0
    while i < k:
        last_element = nums.pop()
        print(last_element)
        nums.insert(0, last_element)
        i += 1
    return nums


nums5 = [1, 2, 3, 4, 5, 6, 7]
k = 2

# print(rotate(nums5, k))
