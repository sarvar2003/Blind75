class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0] * (m+1)

        for i in range(1, n+1):
            new = [0] * (m+1)
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    new[j] = 1 + dp[j-1]
                else:
                    new[j] = max(new[j-1], dp[j])
            dp = new

        return dp[m]

# Time: O(m*n)
# Space: O(m)

# n, m = len(text1), len(text2)