import math
"""
Not complete

"""
def mergeSort(data,):
    print(data)
    
    m=int(math.floor(len(data)/2))
    if len(data)==1:
        return data
    mergeSort(data[0:m-1])
    mergeSort(data[m:])
    return 0
# def merge(a,b):

data = [8,9,5,4,3,2,1,3,5,7,3,8]

# print(mergeSort(data))
m=int(math.floor(len(data)/2))
print(m)
print(data[0:m-1])
print(data[m:])