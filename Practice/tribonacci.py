def tribonacci(n):
    res = [0] * (n + 1) # initiliaze the number of items
    res[0] = 0
    res [1] = 1
    res [2] = 1
    counter, i = 0 , 0

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1


    for i in range(3, n + 1):
        res[i] = res[i-1] + res[i-2] + res [i-3]

        
    return res[n]

input = 25
print (tribonacci(input))