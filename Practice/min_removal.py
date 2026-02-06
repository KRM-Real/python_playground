def minRemoval(nums, k):
    
    nums.sort()
    i = 0
    max_length = 0

    for j in range(len(nums)):
        while nums[j] > nums[i] * k:
            i += 1
        max_length = max(max_length, j - i + 1)
        
    return len(nums) - max_length

Input = [1,6,2,9]
k = 3
print(minRemoval(Input,k))