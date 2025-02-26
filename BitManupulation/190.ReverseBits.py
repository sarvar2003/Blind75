class Solution:
    def reverseBits(self, n: int) -> int:
        
        return int(bin(1 << 33 | n)[4:][::-1], 2)

# Time: O(n)
# Space: O(n)