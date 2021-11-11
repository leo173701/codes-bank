

\126. Word Ladder II 单词接龙

参考 \127. [Word Ladder](https://leetcode.com/problems/word-ladder/)  找最短路径的长度是多少？

```python
#Input: 
beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log","cog"]
#Output: 
[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

![image](https://assets.leetcode.com/users/images/b922ec67-ab63-4768-beb5-ad108083c4c9_1627123895.1947684.png)





```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        wordset.add(endWord)
        wordset.add(beginWord)  #通过集合扩容的形式，把起点和终点也包括进来。
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
        # 回溯法，把各个 combination 写下来。
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
        # 求集合当中的各个点， 到 start 的距离。
        # 小心 一定要找到最短距离。
        distance[start]=0
        q = deque([start])
        while q:
            cur_word = q.popleft()
            for nextword in next_words[cur_word]:
                if nextword not in distance:
                    distance[nextword] = distance[cur_word]+1 # 这里或许还能再优化
                    q.append(nextword)
    
    def get_next_words(self,word,wordset):
        # 在wordset 当中 找到word 可能的合理的 变异体
        mutations=[]
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                mutation = word[:i]+char+word[i+1:]
                if mutation!=word and mutation in wordset:
                    words.append(mutation)
        return mutations    
```



- 
- This problem is an advanced version of **[127. Word Ladder](https://leetcode.com/problems/word-ladder/)**, I highly recommend solving it first if you haven't solved it yet.
- To find the shortest path from `beginWord` to `endWord`, we need to use BFS.
- To find neighbors of a `word`, we just try to change each position from the original `word`, each position we try to change letters from `a..z`, the neighbors are valid if and only if they're existed in the `wordList`.
- The problem is required to output the answer sequence paths, so we need to store sequences path so far while doing bfs.
  - Let `level[word]` is the all possible sequence paths which start from `beginWord` and end at `word`.
  - Then `level[endWord]` is our answer.

# ***神一般的存在！***

```python
# https://leetcode.com/problems/word-ladder-ii/discuss/1359027/C%2B%2BPython-BFS-Level-by-Level-with-Picture-Clean-and-Concise
class Solution:  # 44 ms, faster than 86.16%
    def findLadders(self, beginWord, endWord, wordList) -> List[List[str]]:
        wordSet = set(wordList)  # to check if a word is existed in the wordSet, in O(1)
        wordSet.discard(beginWord)

        def neighbors(word):
            for i in range(len(word)):  # change every possible single letters and check                                        # if it's in wordSet
                for c in ascii_lowercase:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        yield newWord

        level = {}
        level[beginWord] = [[beginWord]]  # level[word] is all possible sequence paths                                             which start from beginWord and end at `word`.
        while level:                      #并没有明显的queue 存在
            nextLevel = defaultdict(list)
            for word, paths in level.items():
                if word == endWord:
                    return paths  # return all shortest sequence paths
                for nei in neighbors(word):
                    for path in paths:
                        nextLevel[nei].append(path + [nei])  # form new paths with `nei`                                                              # word at the end
            wordSet -= set(nextLevel.keys())  # remove visited words to prevent loops
            level = nextLevel                              # move to new level

        return []
```





#求路径的标准写法： 找前驱。

```python
class Solution(object):
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # Write your code here
        dict.add(start)
        dict.add(end)

        def buildPath(path,word):
            if len(preMap[word]) == 0:			#如果当前单词没有前驱，word已经是第一个点
                result.append([word] + path)	#将word和path存入结果即可
                return
            path.insert(0,word)                 #将word插入到0位置
            for w in preMap[word]:				#对当前word里面的所有前驱枚举
                buildPath(path,w)				#继续搜索
            path.pop(0)							#搜索完成后弹出

        length = len(start)
        preMap = {}
        for word in dict:
            preMap[word] = []       #初始化，每一个点的有一个前驱 list
        result = []
        cur_level = set()
        cur_level.add(start)

        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                dict.remove(word)    # 删除掉 结合中 在上一层用过的所有的点
            for word in pre_level:   # 遍历上一层所有的点， 用for循环 不用queue
                                     # 直接实现了分层queue 
                for i in range(length):
                    left = word[:i]				#取出当前单词左部分
                    right = word[i+1:]			#取出当前单词右部分
                    for c in 'abcdefghijklmnopqrstuvwxyz':		#枚举当前替换单词
                        if c != word[i]:
                            nextWord = left + c + right			#组成新单词
                            if nextWord in dict:				#如果新单词在dict里面
                                preMap[nextWord].append(word)   #nextWord的前驱为word
                                cur_level.add(nextWord)			#word的下一个单词为nextWord
            if len(cur_level) == 0:  # 到达终点
                return []
            if end in cur_level:
                break                # 何时停止？ 找到终点就停止， 所以cur_level 使用了集合。
        buildPath([],end)
        return result
```

