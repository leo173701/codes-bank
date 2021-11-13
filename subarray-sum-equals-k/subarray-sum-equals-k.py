class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        res = 0
        for i in range(1,len(nums)):
            nums[i] +=nums[i-1]
        for presum in nums:
            if presum-k in dic:
                res +=dic[presum-k]
            dic[presum] = dic.get(presum,0)+1
        return res