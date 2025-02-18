class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        suffixProduct = []
        suffix = 1
        for i in range(n):
            suffix *= nums[n-i-1]
            suffixProduct.append(suffix)
        
        suffixProduct.reverse()

        prefix = 1
        for i in range(n):
            product = 1
            product *= prefix
            
            if i < n-1:
                product *= suffixProduct[i+1]
            
            suffixProduct[i] = product
            prefix *= nums[i]

        return suffixProduct

# Time: O(n)
# Space: O(1)