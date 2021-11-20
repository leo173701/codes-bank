\90. Subsets II

求子集

需要去重，空集也算

```python
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        visited = [False for i in range(n)]
        def dfs(nums, path, start):
            res.append(path[:])
            for i in range(start, n):
                if visited[i] :
                    continue
                if i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
                    continue
                visited[i]=True
                path.append(nums[i])
                dfs(nums, path, i+1)
                path.pop()
                visited[i]=False
        dfs(nums,[],0)
        return res
```

