def fibonacci_number(n):
    
    f1 , f2 = 0 , 1
    counter = 0
    
    while counter < n-1:
        res = f1 + f2
        print(f1, f2)
        #Update
        counter += 1
        f1 = f2
        f2 = res

    return res

input = 4
print (fibonacci_number(input))
        