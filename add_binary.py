
def transform_binary(a):
    sum_value = 0
    for i in range(len(a)):
        if(a[i]=="1"):
            sum_value = 2 ** (len(a)-i-1) + sum_value
        
    return sum_value

def add_binary(a,b):
    a_decimal = transform_binary(a)
    b_decimal = transform_binary(b)
    sum_decimal = a_decimal+b_decimal
    
    binary = ""
    if sum_decimal>0:
        while sum_decimal>0:
            sum_mod = sum_decimal%2
            sum_decimal = sum_decimal//2
            binary = str(sum_mod)+binary
    else:
        return "0"
    return binary

def main():
    print(add_binary("1110","1111"))





if __name__=="__main__":
    main()
