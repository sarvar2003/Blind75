class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJumpInd = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= canJumpInd:
                canJumpInd = i

        return canJumpInd == 0

# Time: O(n)
# Space: O(1)