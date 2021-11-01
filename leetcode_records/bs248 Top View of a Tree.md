

## Top View of a Tree

https://binarysearch.com/problems/Top-View-of-a-Tree



![image-20211101150548417](C:/Users/leo17/AppData/Roaming/Typora/typora-user-images/image-20211101150548417.png)

BFS 做法：

1. BFS遍历，同时用res记录结果
2. 维护一个locations 数组来判断这个结点的相对位置，如果它比最左边的还左边（loc<locations[0])，那就插进左侧； 如果它比最右边的还右边（loc>locations[-1]），那就添加在最右侧。
3. 每次加入queue的时候插入（cur.left,  loc-1）或者 （cur.right, loc+1）

```python
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return []
        q = collections.deque([(root,0)])
        locations = []
        res = []
        while q:
            for _ in range(len(q)):
                cur, loc = q.popleft()
                if not locations or loc > locations[-1]:
                    locations.append(loc)
                    res.append(cur.val)
                elif loc< locations[0]:
                    locations.insert(0,loc)
                    res.insert(0,cur.val)
                if cur.left:
                    q.append((cur.left,loc-1))
                if cur.right:
                    q.append((cur.right,loc+1))
        return res
```



