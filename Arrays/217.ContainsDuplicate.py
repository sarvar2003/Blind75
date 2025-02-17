class Solution:
    def containsDuplicateS1(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        
        return False

    # Time: O(nlogn)
    # Space: O(1)

    def containsDuplicateS2(self, nums: List[int]) -> bool:
        
        return not len(nums) == len(set(nums)) 
    
    # Time: O(n)
    # Space: O(n)

        