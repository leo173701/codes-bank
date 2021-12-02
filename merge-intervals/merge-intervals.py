from functools import cmp_to_key
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  
           
        if intervals == []:
            return []
      
        # 按照区间start进行排序
        intervals = sorted(intervals, key=lambda interval: (interval[0],interval[1]))
        
        result = []
        last_interval = intervals[0]
        
        # 如果两段区间有交集的话，合并两段区间
        # 没有的话，将最后的区间加入答案，并令新的区间作为最后的区间
        for i in range(1, len(intervals)):
            if self.have_intercation(last_interval, intervals[i]):  #如果有交集
                last_interval = self.merge_two_intervals(last_interval, intervals[i])
            else:
                result.append(last_interval)
                last_interval = intervals[i]  #这里变成重点
        result.append(last_interval)
        
        return result
    
    
    # 合并两段区间
    def merge_two_intervals(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]
    
    # 判断区间是否有交集，要满足较大的start小于等于较小的end
    def have_intercation(self, a, b):
        return max(a[0], b[0]) <= min(a[1], b[1]);
