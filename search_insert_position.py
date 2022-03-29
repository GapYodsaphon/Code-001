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


def searchInsert (nums, target) :

    l,r = 0,len(nums)-1

    insert_loc = 0
    while l<r :
        if nums[l]==target:
            return l 
        elif nums[r]==target:
            return r
        l+=1
        r-=1

    for i in range(len(nums)):
        if nums[i]<target:
            insert_loc = i+1

    return insert_loc

print(searchInsert([1,3,5,6],0))


"""
Fast Solution
min = 0
max = len(nums)-1  
        while min <= max:
            mid = (min+max)//2 #rounds down
            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    max = mid-1
                else:
                    min = mid+1
return min      

"""
