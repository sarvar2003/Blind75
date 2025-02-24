class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for num in nums:

            temp = curMax * num
            curMax = max(temp, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            res = max(res, curMax)

        return res

# Time: O(n)
# Space: O(1)