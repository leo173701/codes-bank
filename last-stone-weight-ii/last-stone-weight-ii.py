class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        if len(stones)==1:
            return stones[0]
        temp = {stones[0], - stones[0]}
        for stone in stones[1:]:
            # print("stone =",stone)
            temp2 = set()
            for i in temp:
                a = i+stone
                b = abs(i-stone)
                if a not in temp2 and a>=0:
                    temp2.add(a)
                if b not in temp2 and b>=0:
                    temp2.add(b)
            temp = temp2
            # print("   ",temp)
        return min(temp)