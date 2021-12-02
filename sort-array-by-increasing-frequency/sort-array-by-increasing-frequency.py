class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        # print(dic)
        temp = sorted([(frequency, -i) for i,frequency in dic.items()])
        # print(temp)
        res = []
        for frequency, i in temp:
            res +=[-i]*frequency
        return res