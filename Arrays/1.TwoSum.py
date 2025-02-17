class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(nums)):
            remainder = target-nums[i]
            
            if remainder in cache:
                return [cache[remainder], i]
            
            cache[nums[i]] = i