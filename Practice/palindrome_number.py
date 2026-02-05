def isPalindrome(x):
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
sol = isPalindrome(x)
print(sol)


# Main Logic for Checking Palindrome Number
# Reverse the number and compare with original
# rev = rev * 10 + x % 10
#            x //= 10
