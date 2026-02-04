class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse = 0
        copy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            print(reverse, copy)
            x //= 10

        return reverse == copy

x = 121
sol = Solution()
print(sol.isPalindrome(x))


# Main Logic for Checking Palindrome Number
# Reverse the number and compare with original
# rev = rev * 10 + x % 10
#            x //= 10
