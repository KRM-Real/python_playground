def minDeletion(self, nums):
       
    res = []
        
    for x in nums:
        if len(res) % 2 == 0 or x != res[-1]:
            res.append(x)

    return len(nums) - (len(res) - len(res) % 2 )