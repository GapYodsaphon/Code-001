import re


regis_list = []
print("Enter Number of candidate : ",end="")
candidate_num = int(input())


for i in range(candidate_num):
    regis_list.append(0)
# สำหรับบัตรเสีย
regis_list.append(0)
vote_n = 0
while vote_n!="q":
    print("vote candidate ",end="")
    vote_n = input()
    if vote_n != "q":
        vote_n = int(vote_n)
        if vote_n>candidate_num or vote_n<1:
            regis_list[-1]+=1
        for i in range(candidate_num):
            if vote_n ==i+1:
                regis_list[i]+=1
        


print("Result Vote Is ")
for i in range(len(regis_list)):
    if i==len(regis_list)-1:
        print("บัตรเสีย เท่ากับ",regis_list[i])
    else:
        print("Number",i,"Vote is",regis_list[i])
    