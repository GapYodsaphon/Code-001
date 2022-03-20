"""

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""


nums = [0,0,1,1,1,2,2,3,3,4]
i=1
# while i<len(nums):
    # print(nums[i-1],nums[i])
   # if nums[i-1]==nums[i]:
    #     if i==1:
    #         for idx in range(1,len(nums)):
                
    #             nums[idx-1]=nums[idx]
            
    #         nums[idx] = "_"
    #         i=i-1
    #     elif i == len(nums)-1:
    #         nums[i] = "_"
    #         i=i+1
    #     else:
    #         for index in range(i+1,len(nums)):
    #             nums[index-1]=nums[index]  
    #         nums[index]="_"
    #         i-=1
        
    #     i=i+1
        
    # i+=1        

i=0
for j in range(len(nums)):
    if(nums[j]!=nums[i]):
        i+=1
        nums[i]=nums[j]
        
print(nums)
print(i+1)