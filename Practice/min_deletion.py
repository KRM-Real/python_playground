# Problem: Minimum Deletion to make String Balance
# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced.
# s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.

# Input: s = "aababbab"
# Output: 2

def minimumDeletions(s):
        res = len(s)
        a, b = 0, 0
        
        
        for c in s:
            a += (c == 'a')
            
        for c in s:
            a -= (c == 'a')
            res = min(res, a + b)
            b += (c == 'b')

        return res
    
input = "aababbab"
print(minimumDeletions(input))