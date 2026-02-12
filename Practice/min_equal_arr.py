def minMoves(nums):
       
    return sum(nums) - min(nums) * len(nums)

input = [1,2,3]
print(minMoves(input))