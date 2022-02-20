class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            a=target-nums[i]
            if target-nums[i] in dic:
                return [i, dic[a]]
            else:
                dic[nums[i]]=i