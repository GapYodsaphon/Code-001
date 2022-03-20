nums = [-4,-1,0,3,10]

for i in range(len(nums)):
    nums[i] = nums[i]*nums[i]

l,r = 0,len(nums)-1
nums = nums.sort()
print(nums)
