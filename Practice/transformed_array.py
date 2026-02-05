#Problem Statement
# You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

# For each index i (where 0 <= i < nums.length), perform the following independent actions:
# If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.

# Input: nums = [3,-2,1,1]
# Output: [1,1,1,3]

def constructTransformedArray (nums):
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] > 0:
                result[i] = nums[(i + nums[i]) % n]
            elif nums[i] < 0:
                result[i] = nums[(i - abs(nums[i])) % n]
            else:
                result[i] = 0

        return result
    
num = [3,-2,1,1]
print(constructTransformedArray(num))