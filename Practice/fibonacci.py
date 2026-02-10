def fibonacci_number(n):
    
    f1 , f2 = 0 , 1
    counter, res = 0, 0
    
    while counter < n-1:
        res = f1 + f2
        print(f1, f2)
        #Update
        counter += 1
        f1 = f2
        f2 = res

    return res

input = 2
print (fibonacci_number(input))
        
        
    # Time : O(n)
    # # Mem : O(n)
    # if n == 0:return 0
    # if n==1 : return 1
    # fib_memo = {0:0,1:1}
    # for i in range(2,n+1):
    # fib_memo[i] = fib_memo[i-2]+fib_memo[i-1]
    # return fib_memo[n]