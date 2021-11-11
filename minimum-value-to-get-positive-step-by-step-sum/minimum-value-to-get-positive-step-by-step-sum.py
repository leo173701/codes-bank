class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        temp = 0
        minvalue = float('inf')
        for i in nums:
            temp +=i
            minvalue = min(minvalue, temp)
        if minvalue>0:
            return 1
        else:
            return 1- minvalue