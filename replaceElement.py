
from asyncio.windows_events import NULL


arr = [17,18,5,4,6,1]

for i in range(len(arr)):
    max_num=0
    for j in range(i+1,len(arr)):
        
        if (j == i+1):
            max_num = arr[j]
            print("init",max_num)
            
        elif max_num < arr[j]:
            max_num = arr[i+1]
        if j == len(arr)-1:
            arr[i+1] = max_num
        print("num ",arr[j])
    print()
    print(max_num)
    print()
    if i==len(arr)-1:
        arr[i]=-1
print(arr)