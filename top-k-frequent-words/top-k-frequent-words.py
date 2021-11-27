class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp = {}
        for word in words:
            temp[word]=temp.get(word,0)+1
        heaplist = [(-frequency, word) for word, frequency in temp.items()]
        heapq.heapify(heaplist)
        res = []
        for i in range(k):
            frequency, word = heapq.heappop(heaplist)
            res.append(word)
        return res