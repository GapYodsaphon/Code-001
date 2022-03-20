arr = [10,2,5,3]


for i in range(len(arr)):
     for j in range(len(arr)):
         if i!=j and arr[i]==arr[j]*2:
             print(True)