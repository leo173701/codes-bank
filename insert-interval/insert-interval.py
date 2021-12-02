class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda interval: (interval[0],interval[1]))
        
        result = []
        for interval in intervals:
            if len(result)==0 or (result[-1][1]<interval[0]):
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
        return result