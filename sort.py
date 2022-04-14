def sort(arr):
    for i in range(len(arr)-1):
        # check ทีละ index
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
        
    return arr


print(sort([4,5,9,2,7,1]))
