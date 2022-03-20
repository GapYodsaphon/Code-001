
#two pointer technique
"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Input: nums = [0]
Output: [0]
"""

# 
import re
from nbformat import read


nums = [0,1,0,3,12]
# nums = [2,1]

# read_ptr =0
write_ptr =0

for read_ptr in range(len(nums)):
        if nums[read_ptr]!=0:
                nums[write_ptr]=nums[read_ptr]
                write_ptr+=1

for zero in range(write_ptr,len(nums)):
        nums[zero]=0

print(nums)