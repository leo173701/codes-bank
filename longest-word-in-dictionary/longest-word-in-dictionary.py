class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words.sort(key = len, reverse = True)
        res = []
        for word in words:
            temp = word
            i = 1
            for i in range(len(temp)):
                if temp[:len(temp) - i] in words:
                    if i == len(temp) - 1:
                        return temp
                    continue
                else:
                    break       
        return ''