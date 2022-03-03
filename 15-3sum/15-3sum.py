class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<3 or not nums:
            return []
        nums.sort()#不知道怎么做的时候，排个序
        res = []
        for i in range(n):
            if nums[i]>0:
                return res #没戏了，三数全都大于0， 三数字之和不可能等于0
            if i>0 and nums[i]==nums[i-1]: #加快一点
                continue
            left = i+1
            right = n-1
            while left<right:
                if nums[i]+nums[left]+nums[right] ==0:
                    res.append([nums[i],nums[left],nums[right]]) #可能结果有很多组
                    while (left<right and nums[left]==nums[left+1]): #避开重复的内容
                        left+=1
                    while (left<right and nums[right]==nums[right-1]):
                        right -=1
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right] <0:
                    left+=1
                else:
                    right-=1
        return res
        