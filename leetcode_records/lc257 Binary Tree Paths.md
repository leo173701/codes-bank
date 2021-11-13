\257. Binary Tree Paths

![img](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)

```python
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        stack = [(root, str(root.val))]
        while stack:            
            cur, path = stack.pop()
            print(cur.val,  path)
            if not cur.left and not cur.right:
                res.append(path)
            if cur.left:
                stack.append((cur.left, path+"->"+str(cur.left.val)))
            if cur.right:
                stack.append((cur.right, path+"->"+str(cur.right.val)))
        return res
```

