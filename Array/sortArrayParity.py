"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Input: nums = [0]
Output: [0]
"""

nums = [3,1,2,4]
nums = [0]
write_ptr = 0
for i in range(len(nums)):

    if nums[i]%2==0:
        tmp = nums[write_ptr]
        nums[write_ptr]=nums[i]
        nums[i] =tmp
        write_ptr+=1

print(nums)
    
