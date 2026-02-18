def findGCD(nums):

    # Most optimal
        a = min(nums)
        b = max(nums)
        while( b!=0):
            temp=b
            b =a%b
            a=temp
        return a
    

num = [3, 3]
print(findGCD(num))

  # small = min(nums)
    # high = max(nums)
    # gcd = 0
    
    # for i in range(1, max(nums)+1):
    #     if (small % i) == 0 and (high % i) == 0:
    #         gcd = i
    
    # while (high !=0):
    #     temp = high
    #     high = small % high
    #     small = temp
    
    #    return gcd