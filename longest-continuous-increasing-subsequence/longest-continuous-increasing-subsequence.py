class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
        res = 1
        temp = 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                temp +=1
                res = max(res, temp)
            else:
                temp=1
        return res        