class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(left: int, right: int) -> int:
            rob1, rob2 = 0, 0

            for i in range(left, right):
                temp = max(rob1+nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(solve(0, len(nums)-1), solve(1, len(nums)))

# Time: O(n)
# Space: O(1)