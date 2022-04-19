def sort(arr):
    for i in range(len(arr)):
        # check ทีละ index
        # แต่ละ i จะ ได้ 1 ตัว ซ้ายสุดที่มากสุดและลำดับไม่เปลี่ยนละ
        for j in range(len(arr)-1-i):
            
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


print(sort([4,5,222,9,2,7,1]))
