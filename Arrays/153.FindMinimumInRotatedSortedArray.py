class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1

        while left < right:
            mid = (right+left) // 2

            if left+1 == right:
                return min(nums[left], nums[right])
            
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return nums[left]
            
        return nums[0]

# Time: O(logn)
# Space: O(1)