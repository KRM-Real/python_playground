def insertPosition(nums, target):
    
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)/2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l


num = [1,3,5,6]
target_num = 7
print(insertPosition(num, target_num))


# Not Optimal and not O(log n)
    # if target > nums[-1]:
    #     return len(nums)
    
    # if target < nums[0]:
    #     return 0
    
    # for i in range(0, len(nums)):
    #     if target == nums[i]:
    #         return i
        
    #     if target < nums[i] and target > nums[i - 1]:
    #         return i