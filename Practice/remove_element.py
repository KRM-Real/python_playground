def removeElement(nums,val):
    
    i = 0
    
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
        
    
    return i

arr = [2,3,3,2]
remove = 3
print(removeElement(arr, remove)) 