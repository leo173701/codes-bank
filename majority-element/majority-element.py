class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        temp = collections.Counter(nums)
        for i,frequency in temp.items():
            if frequency > n//2:
                return i