def maximizeExpressionOfThree(nums):
    

        # nums.sort()
        # return nums[-1] + nums[-2] - nums[0]
        
        max1 = max2 = float('-inf')
        min_val = float('inf')

        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n

            if n < min_val:
                min_val = n

        return max1 + max2 - min_val

input = [-2,0,5,-2,4]
print(maximizeExpressionOfThree(input))