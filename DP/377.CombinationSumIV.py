class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(target: int, res: int) -> int:
            if target == 0:
                return 1
            
            if target < 0:
                return 0

            if target in memo:
                return memo[target]
            
            res = 0 
            for n in nums:
                res += dp(target-n, res)
            
            memo[target] = res
            return res
        
        return dp(target, 0)
    
    def combinationSum4II(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        
        for i in range(1, target+1):
            for n in nums:
                if i - n < 0:
                    continue
                if i - n == 0:
                    dp[i] += 1
                dp[i] += dp[i-n]
        
        return dp[target]

# Time: O(n*t)
# Space: O(t)

# n, t: len(nums), target