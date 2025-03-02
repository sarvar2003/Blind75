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

# Time: O(n*t)
# Space: O(t)

# n, t: len(nums), target