class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for num in nums:
            res ^= (n ^ num)
            n -= 1
        
        res ^= n

        return res

# Time: O(n)
# Space: O(1)