class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        left, right, curArea = 0, len(height)-1, 0
        while left < right:

            if height[left] > height[right]:
                curArea = height[right] * (right-left)
                right -= 1
            else:
                curArea = height[left] * (right-left)
                left += 1

            res = max(res, curArea)

        return res

# Time: O(n)
# Space: O(1)