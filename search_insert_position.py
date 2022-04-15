"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1


Runtime: 84 ms
Memory Usage: 14.7 MB
"""

# Normal


def searchInsert(nums, target):

    l, r = 0, len(nums)-1

    insert_loc = 0
    while l < r:
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        l += 1
        r -= 1

    for i in range(len(nums)):
        if nums[i] < target:
            insert_loc = i+1

    return insert_loc


print(searchInsert([1, 3, 5, 6], 0))


# ----> Binary Search Way
def searchInsertBinary(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        m = (left+right)//2
        if nums[m] == target:
            return m
        elif target > nums[m]:
            left = m+1
        elif target < nums[m]:
            right = m-1
    return left

print(searchInsertBinary([1, 3, 5, 6], 0))