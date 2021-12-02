class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        # print(dic)
        heap = []
        for i,value in dic.items(): 
            heapq.heappush(heap,(-value,i))
        res = ""
        while heap:
            value, i = heapq.heappop(heap)
            res +=i* (-value)
        return res
        