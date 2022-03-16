
arr = [1,5,1,3,6,1]
k=3
sum_arr =[]

print(len(arr)-(k-1))
for i in range(0,len(arr)-(k-1)):
    sum_a = 0    
    for j in range(k):
        # print(j+i)
        sum_a = arr[j+i]+sum_a
    sum_arr.append(sum_a)
print(sum_arr)
for i in range(len(sum_arr)):
    if i ==0:
        max_num = sum_arr[0]
    if max_num< sum_arr[i]:
        max_num = sum_arr[i]


print(max_num)