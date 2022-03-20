


data = [6,565,5,4,2,3,1]

for i in range(len(data)):
    for j in range(i):
        # print(i,j)
        if(data[i]<data[j]):
            tmp = data[j]
            data[j]=data[i]
            data[i]=tmp
print(data)
    # for j in range(len(data)-i):
    #     j = j+i
    #     print(i,j)
    