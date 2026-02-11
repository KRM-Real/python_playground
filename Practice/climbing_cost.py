def minCostClimbingStairs(cost):
        if not cost:
            return 0
        
        cur=0
        dp0=cost[0]
        
        if len(cost) >= 2:
            dp1=cost[1]
        
        for i in range(2, len(cost)):
            cur=cost[i] + min(dp0,dp1)
            dp0=dp1
            dp1=cur
            
        return min(dp0,dp1)
    
input = [1,100,1,1,1,100,1,1,100,1]
print (minCostClimbingStairs(input))