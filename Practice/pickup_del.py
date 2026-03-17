# 1359. Count All Valid Pickup and Delivery Options
# Given n orders, each order consists of a pickup and a delivery service.
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
# Since the answer may be too large, return it modulo 10^9 + 7.

# Example 1:

# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

def countOrders(self, n):
        
        ans = 1
        
        for n in range(2, n + 1):
            ans *= n*(2*n-1)
            ans %= (10**9+7)

        return ans