
arr = [1,5,2,0,6,8,0,6,0]
j=0
i=0
while i < len(arr):
    if arr[i]==0 :
        j=0
        
        for j in range(len(arr)-1,i+1,-1):
            arr[j]= arr[j-1]
        arr[j-1]=0
        
        if (i==len(arr)):
            print("last")

        i+=1
        
        
    i+=1     
        
        
    

print(arr)