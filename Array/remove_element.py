"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""
#testcase
nums=[3,2,2,3]
val =3
nums = [0,1,2,2,3,0,4,2]
val = 2
# nums = [1]
# val = 1

# nums=[3,3]
# val= 3
# nums = [4,5]
# val = 4
nums = [3,1,3,3,3]
val =3
print(nums)
i=0
while i<len(nums):
    
    # remove
    if val ==nums[i]:
        # check 1st index 
        
        if i==0:
            index=0
            for index in range(1,len(nums)):
                nums[index-1]=nums[index]
            nums[index]="_"
            i-=1
        #check last
        elif i==len(nums):
            nums[i]="_"
            
        #every index
        else:
            for idx in range(i+1,len(nums)):
                nums[idx-1]=nums[idx]
            nums[idx]="_"
            i-=1
    i+=1
        
    
count = 0
for ix in range(len(nums)):
    if nums[ix]=="_":
        continue
    else:
        count+=1
print(count)


print(nums)


"""
easy way
i = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                

"""