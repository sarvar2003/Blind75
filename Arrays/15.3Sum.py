class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        n = len(nums)
        for i in range(n-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n-1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

# Time: O(n^2)
# Space: O(1)