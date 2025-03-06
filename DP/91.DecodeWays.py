class Solution:
    def numDecodings(self, s: str) -> int:
        s1, s2 = 1, 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                s2 = s1
                s1 = 0
                continue
            
            temp = s1
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                s1 += s2
            
            s2 = temp
        
        return s1

# Time: O(n)
# Space: O(1)