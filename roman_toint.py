s="MCMXCIV"
int_num =0
i=0
if(s[i]=="I"):
    int_num += 1
elif(s[i]=="V"):
    int_num += 5
elif(s[i]=="X" ):
    int_num+=10
elif(s[i]=="L" ):
    int_num+=50
elif(s[i]=="C"):
    int_num+=100
elif(s[i]=="D"):
    int_num+=500
elif(s[i]=="M"):
    int_num+=1000
print(s[i],"=",int_num)   
for i in range(1,len(s)):
    
    if(s[i]=="I"):
        int_num += 1
    elif(s[i]=="V" and s[i-1]!="I"):
        int_num += 5
    elif(s[i]=="V" and s[i-1]=="I"):
        int_num+=4
        int_num-=1
    elif(s[i]=="X" and s[i-1]!="I"):
        int_num+=10
    elif(s[i]=="X" and s[i-1]=="I"):
        int_num+=9
        int_num-=1
    elif(s[i]=="L" and s[i-1]!="X"):
        int_num+=50
    elif(s[i]=="L" and s[i-1]=="X"):
        int_num+=40
        int_num-=10
    elif(s[i]=="C" and s[i-1]!="X"):
        int_num+=100
    elif(s[i]=="C" and s[i-1]=="X"):
        int_num+=90
        int_num-=10
    elif(s[i]=="D" and s[i-1]!="C"):
        int_num+=500
    elif(s[i]=="D" and s[i-1]=="C"):
        int_num+=400
        int_num-=100
    elif(s[i]=="M" and s[i-1]!="C"):
        int_num+=1000
    elif(s[i]=="M" and s[i-1]=="C"):
        int_num+=900
        int_num-=100
    print(s[i],"=",int_num)


print(int_num)