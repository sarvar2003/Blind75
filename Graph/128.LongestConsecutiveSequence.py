class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited, nums = set(), set(nums)
        res = 0

        for num in nums:
            cur = 0
            if num-1 in nums:
                continue
                
            while num in nums and num not in visited:
                visited.add(num)
                cur += 1
                num += 1

            res = max(res, cur)
        
        return res
    
# Time: O(n)
# Space: O(n)