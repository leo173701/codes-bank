class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        dic = {}
        for word in words:
            dic[word]=dic.get(word,0)+1
        temp = sorted(dic.items(), key=lambda item: (-item[1], item[0].lower()))
        return [temp[i][0] for i in range(k)]
       