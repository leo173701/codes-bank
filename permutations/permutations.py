class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums,[],res)
        return res
    
    
    def helper(self,nums,track, res):
        if len(track)==len(nums):
            res.append(list(track))      
        for i in nums:
            if i in track:
                continue
            track.append(i)
            self.helper(nums,track,res)
            track.pop()            