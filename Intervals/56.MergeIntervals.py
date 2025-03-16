class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()

        curStart, curEnd = intervals[0]
        curInterval, res = [], []

        for start, end in intervals:
            if start <= curEnd:
                curEnd = max(curEnd, end)
            else:
                res.append(curInterval)
                curStart, curEnd = start, end

            curInterval = [curStart, curEnd]
        
        res.append(curInterval)

        return res

# Time: O(nlogn)
# Space: O(n)