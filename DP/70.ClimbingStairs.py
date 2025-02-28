class Solution:
    def climbStairs(self, n: int) -> int:
        oneBelow, twoBelow = 1, 0

        for _ in range(n):
            temp = oneBelow
            oneBelow += twoBelow
            twoBelow = temp
        
        return oneBelow

# Time: O(n)
# Space: O(1)
