class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        res = 1
        wordslist = sorted(words, key=lambda x:len(x))
        # print(wordslist)

        dp=[1]*n
        for i,word in enumerate(wordslist):
            for j in range(i):
                if len(wordslist[j])+1==len(word):
                    for k in range(len(word)):
                        if word[:k]+word[k+1:]==wordslist[j]:
                            dp[i] = max(dp[i],dp[j]+1)
                            # print(word[:k]+word[k+1:],  "==",wordslist[j] )
            res = max(res, dp[i])
        return res