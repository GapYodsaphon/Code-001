


# strs = ["flower","flow","flight"]
sara = ['a','e','i','o','u']
# strs = ["flower","flow","flight"]
strs=['a']

# strs = ["dog","racecar","car"]
# count_str=0
for i in range(len(strs)):
    count_str=0
    for j in range(len(strs[i])):
        if (strs[i][j]==sara[0] or strs[i][j]==sara[1] or strs[i][j]==sara[2] or strs[i][j]==sara[3] or strs[i][j]==sara[4]) :
            if count_str <=1:
                count_str=0 
            elif count_str>1:
                word = strs[i][j-2:count_str]
                count_str=0       

        # if count_:
        #         print('\nprefix is ',strs[i][j])
        else:
            count_str+=1
            
        
    

