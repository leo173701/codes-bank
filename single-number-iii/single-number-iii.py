class Solution:
    def singleNumber(self, A: List[int]) -> List[int]:
        s = 0
        for x in A:
            s ^= x
        y = s & (-s)

        ans = [0,0]
        for x in A:
            if (x & y) != 0:
                ans[0] ^= x
            else:
                ans[1] ^= x                 
        return ans