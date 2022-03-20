
# Done But Bruteforge 

arr = [17,18,5,4,6,1]

for i in range(len(arr)):
    
    for j in range(i+1,len(arr)):
        if (j == i+1):
            max_num = arr[j]
            
        if max_num < arr[j]:
            max_num = arr[j]
            
        if j == len(arr)-1:
            arr[i] = max_num
            max_num=0
        
        
    if i==len(arr)-1:
        arr[i]=-1
print(arr)