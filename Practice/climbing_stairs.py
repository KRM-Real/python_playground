def climbStairs(n):
        
    res = [0] * (n + 1) # Assign the first index as index 1, initiliaze the number of items
    res[0] = 0
    res [1] = 1

    for i in range(1, n):
        res[i] = res[i - 1] + res [i - 2] # Fibonnaci Logic 
        print(res[i])
        
    return res[i]

input = 4
print (f"Result: {climbStairs(input)}")