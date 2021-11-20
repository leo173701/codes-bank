\78. Subsets

```python
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

DFS 回溯

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, nums, path):
            res.append(path[:])
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i+1,nums,path)
                path.pop()
        res = []
        dfs(0,nums,[])
        return res
```

