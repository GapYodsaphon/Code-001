

"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

before refactor :
113 / 113 test cases passed.
Status: Accepted
Runtime: 38 ms
Memory Usage: 14.1 MB


new refactor
113 / 113 test cases passed.
Status: Accepted
Runtime: 67 ms
Memory Usage: 13.9 MB

----------------------------------------------
Conclusion
new refactor less line than old [/]
runtime lower than old [x]
mem usage better than old [/] 

----------------------------------------------
"""
nums = [0,1,2,2,3,0,4,2]
val = 2
# nums = [3,2,2,3]
# val = 3
write_ptr =0

for i in range(len(nums)):
    if nums[i] !=val:
        tmp = nums[write_ptr]
        nums[write_ptr]=nums[i]
        nums[i] = tmp
        write_ptr+=1
    else:
        nums[i]="_"

count = 0
for i in range(len(nums)):
    if nums[i]!="_":
        count+=1
print(count)
print(nums)

