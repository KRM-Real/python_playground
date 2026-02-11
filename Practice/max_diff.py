def maxDifference(nums):
    
        max_counter = -1 # Assign end Element, to start with
        min_counter = nums[0] #Assign first element
    
        for i in range(len(nums)):
            
            max_counter = max(max_counter, nums[i] - min_counter) 
            min_counter = min(min_counter, nums[i])

        if max_counter == 0:
            return -1
    
        return max_counter

input = [7,1,5,4]
print(maxDifference(input))