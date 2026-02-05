def findMedianSortedArrays(nums1, nums2):
        
        #Combine and Sort the two arrays, Get the length 
        merged_nums = sorted(nums1 + nums2)
        length = len(merged_nums)

        if length % 2 == 0:
            return(merged_nums[length // 2 -1] + merged_nums[length // 2]) / 2
        else:
            return merged_nums[length // 2]

num1 = [1,2]
num2 = [3,4]
print(findMedianSortedArrays(num1,num2))

# Work in progress, wrong 