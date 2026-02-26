def merge(nums1, m, nums2, n):

        right = m + n - 1
        midx = m-1
        nidx = n-1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -=1

            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
            
            right -=1
        
        return num1
            
num1 = [1,2,3,0,0,0]
m = 3 

num2 = [2,5,6] 
n = 3

print(merge(num1, m, num2, n))