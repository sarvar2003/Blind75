class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currStock = prices[0]

        for price in prices:
            
            if price < currStock :
                currStock = price
            else:
                profit = max(profit, price-currStock)

        return profit

# Time: O(n)
# Space: O(1)