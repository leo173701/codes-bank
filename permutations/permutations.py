class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(nums, track, res):
            if len(track)==n:
                res.append(track[:])
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                dfs(nums,track,res)
                track.pop()
        dfs(nums,[],res)
        
        return res 