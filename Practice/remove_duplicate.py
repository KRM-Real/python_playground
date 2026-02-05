#Remove Duplicate from Sorted Array

def removeDuplicate(nums):
        i = 1
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                print(nums)
                i += 1
        
        
        return i
    


# Example Given Array : [0,1,1,1,2,2,3,3,4]

array = [0,1,1,1,2,2,3,3,4]
remove = removeDuplicate(array)
print(remove)
