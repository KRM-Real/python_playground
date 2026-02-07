# Problem : You are given a positive number n.
# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

def smallestNumber(n):
    
    res = 0
    while(n>=2**res):
        res+=1
    return (2**res)-1



input = 4
print (smallestNumber(input))