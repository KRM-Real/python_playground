def reverse_int(x):
    
    res = 0
    
    if res < 0:
        res = int(str(x)[1:][::-1]) * 1
    else:
        res = int(str(x)[::-1])
    
    # if res > 2 ** 31 or res < -2 ** 31:
    #     return 0
    
    return res

Input = 1234512345679
print (reverse_int(Input))