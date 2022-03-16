
a=-323
str_a = str(a)


l,r =0,len(str(a))-1

# digit = 0
# for i in range(0,len(str(a))):
#     digit = digit*10
#     if digit ==0:
#         digit =1

# print(digit)
# print(a//digit)
while l<r:
    if str_a[l]==str_a[r]:
        l+=1
        r-=1
    else:
        print(False)
        break
print(True)    

    