class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        res = []

        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]) , max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

# Time: O(n)
# Space: O(n)