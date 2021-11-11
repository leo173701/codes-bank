class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        wordset.add(endWord)
        wordset.add(beginWord)
        next_words = {}
        distance={}
        
        for i in wordset:
            next_words[i] = self.get_next_words(i,wordset)
        # print(next_words)
        self.get_distance(endWord,distance, wordset,next_words)
        # print(distance)
        res = []
        self.dfs(beginWord, endWord,distance, wordset, [beginWord], res,next_words)
        return res
        
    def dfs(self, cur, target, distance, wordset, path, res,next_words):
        if cur==target:
            res.append(list(path))
            return
        for word in next_words[cur]:
            if distance[word]!=distance[cur]-1:
                continue
            path.append(word)
            self.dfs(word,target,distance,wordset,path,res,next_words)
            path.pop()
    
    def get_distance(self, start,distance, wordset,next_words):
        distance[start]=0
        q = deque([start])
        while q:
            cur_word = q.popleft()
            for nextword in next_words[cur_word]:
                if nextword not in distance:
                    distance[nextword] = distance[cur_word]+1
                    q.append(nextword)
    
    def get_next_words(self,word,wordset):
        words=[]
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                temp = word[:i]+char+word[i+1:]
                if temp!=word and temp in wordset:
                    words.append(temp)
        return words    