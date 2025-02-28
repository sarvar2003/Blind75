class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1+dp[a-c])
                else:
                    break

        return dp[amount] if dp[amount] <= amount else -1

# Time: O(c*a) -> 0 <= coins.length <= 12 -> O(a)
# Space: O(a)