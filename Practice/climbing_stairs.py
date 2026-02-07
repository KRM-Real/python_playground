def climbStairs(n):
        
    res = [0] * (n + 1) # Assign the first index as index 1, initiliaze the number of items
    res[0] = 1
    res [1] = 1

    for i in range(2, n + 1):
        res[i] = res[i - 1] + res [i - 2] # Fibonnaci Logic 
        print(res[i])
        
    return res[-1]

input = 7
print (f"Result: {climbStairs(input)}")