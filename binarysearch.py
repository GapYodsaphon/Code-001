import math
def binarySearch(data,value,low,high):
    
    mid = low + (high-low)/2
    mid =math.floor(mid)
    if(low>=high):
        return "not this number in list"

    if(data[mid]>value):
        high = mid
        return binarySearch(data,value,low,high)
    if(data[mid]<value):
        low = mid+1
        return binarySearch(data,value,low,high)
    if(data[mid]==value):
        return mid
    
    # print(data)  
    

data = [1,2,3,4,5,6,7,8,9,10]
find_num = 1
print("idx of number ",find_num," is ",binarySearch(data,find_num,0,len(data)))

