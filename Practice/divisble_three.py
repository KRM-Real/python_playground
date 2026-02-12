def minimumOperations(nums):
    
    counter = 0
    for i in range(0,len(nums)):
        
        # if (nums[i] - 1) % 3 == 0 or (nums[i] + 1) % 3 == 0 or nums[i] == 0:
        #     counter +=1
            
        if (nums[i] % 3) != 0:
            counter +=1

    return counter

input = [1,2,3,4]
print(minimumOperations(input))


#Other Logic:
    #  for i in range(0,len(nums)):
    #      if (nums[i] % 3) != 0
    #         counter +=1