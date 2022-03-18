def validMountainArray(arr) -> bool:
        if len(arr)<3:
            return False
        max_idx =0
        for idx in range(len(arr)):
            if idx ==0:
                max_num = arr[0];
            if max_num<arr[idx]:
                max_num = arr[idx]
                max_idx = idx 


        l,r = 0,len(arr)-1
        if max_idx ==l or max_idx==r:
            return False
        while l<r:
            if max_num > arr[l]:
                l+=1
            if max_num > arr[r]:
                r-=1
            if max_num==arr[l] and max_idx !=l or max_num==arr[r] and max_idx!=r:
                return False
            if(l>0):
                if arr[l]<=arr[l-1]:
                    return False
            if r<len(arr)-1:
                if arr[r]<=arr[r+1]:
                    return False
        return True

print(validMountainArray(arr=[1,2,1]))