def maxProfit(prices):
    
    left = 0     #  Buy
    right = 1    #  Sell
    max_profit = 0
    
    
    while right < len(prices):
        profit = prices[right] - prices[left]
        
        if prices[left] < prices[right]:
            max_profit = max(profit, max_profit)
        else:
            left = right
        
        right += 1
    
    return max_profit

input = [7,1,5,3,6,4]
print (maxProfit(input))

#Better Logic
        # buy_stock= float('inf')
        # max_value=0

        # for price in prices:
        #     if price<buy_stock:
        #         buy_stock= price
        #     else:
        #         max_value=max(max_value, price- buy_stock)