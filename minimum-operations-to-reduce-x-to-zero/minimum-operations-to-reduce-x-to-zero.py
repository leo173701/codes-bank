class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sumvalue = sum(nums)
        if sumvalue<x:
            return -1
        if min(nums)>x:
            return -1
        left = 0
        right = 0
        n = len(nums)
        dic1 = {-1:0}
        temp = 0
        dic2 = {0:-1}
        res = n
        while right <n:
            temp += nums[right]
            # dic1[right] = temp
            dic2[temp]  = right
            # print(dic1)
            # print(dic2)
            goal = temp - (sumvalue - x)
            if goal in dic2.keys():
                res = min(res, n - right + dic2[goal])
                # print("res =",res)
            right +=1
            
        return res        