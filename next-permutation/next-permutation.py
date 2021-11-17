class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2:
            return nums
        loc = n-2
        while nums[loc+1]<=nums[loc] and loc>=0:
            loc-=1
        print("loc = ", loc)
        print(nums[loc], nums[loc+1])
        minvalue = nums[loc+1]
        targetlocation = loc+1
        for i, value in enumerate(nums[loc:]):
            if value > nums[loc]:
                if value < minvalue:
                    minvalue = value
                    targetlocation = i + loc
        print("minvalue = ",minvalue)
        print("targetlocation = ",targetlocation)
        nums[loc], nums[targetlocation] =  nums[targetlocation],nums[loc]
        print(nums)
        a = loc+1
        nums[:]=nums[:a] + sorted(nums[a:])