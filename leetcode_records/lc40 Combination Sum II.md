## combination sum总结：

1. 先排个序

2. 再去下重复  利用集合

3. 如果可以不限次数，那下次就从当前 `i`算起
   `dfs(candidates, remain -candidates[i], path, i)  `

4. 如果限制次数最多一次，那下次就从 `i+1`算起

   `dfs(candidates, remain -candidates[i], path, i+1)`

5. 如果需要考虑path的内部顺序，那就从之前的start开始

    `dfs(candidates, remain -candidates[i], path, start)`

6. 对于求和有两种操作办法：

   ```python
   #1. remain表示还有多少可以剩余
   
   if remain ==0:
       res.append(path[:])
   remain = remain - candidates[i]
   #2. cursum 表示到目前为止积累了多少
   if cursum==target:
       res.append(path[:])
   cursum = cursum + candidates[i]
   ```

   

   

### \39. Combination Sum 每个数字可以重复使用无数次， 输出的结果多个排序只算一个

```python
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```



```python
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```



```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates =sorted( list(set(candidates)))
        n = len(candidates)
        def dfs(candidates, remain, path, start):
            if remain ==0:
                res.append(path[:])
            for i in range(start, n):
                if remain < candidates[i]:
                    break
                path.append(candidates[i])
                dfs(candidates, remain -candidates[i], path, i) #从当前i再次算起
                path.pop()
        dfs(candidates, target, [], 0)
        return res
```







### \40. Combination Sum II

每个元素最多用1次， 求和为target的 组合
跳过重复的数字

```python
输入: num = [7,1,2,5,1,6,10], target = 8
输出: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

使用回溯法搜索所有可能的组合. 很基础的题目, 有多种不同的写法, 再次不多赘述.

有一个显而易见的小优化: 我们在搜索的过程中会记录已经选择的数字的和, 如果这个和超过了 target, 停止搜索. 除此之外还有很多可以优化的细节, 慢慢探索吧!

另外, 这个题目还可以有非递归的形式: 用一个整型的 `num.length` 个二进制位表示一个组合, 第 i 位为 1 表示这个组合内含有 `num[i]`. 这样可以从0自增这个整型来达到枚举所有组合的效果. 避免了递归的开销 (但是也不一定比递归快, 因为递归可以有优化, 而这样枚举就只能老老实实把所有的组合都查看一遍)

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  #不知道怎么做的时候，先排序
        n = len(candidates)
        def dfs(candidates,path,start, cursum):            
            if cursum == target:
                res.append(path[:])
                
            for i in range(start, n):
                if cursum+candidates[i] >target:   #用于剪枝加速算法
                    return
                if (i > start and candidates[i] == candidates[i-1] ):
                    continue  #跳过重复的数字
                    
                path.append(candidates[i])
                dfs(candidates,path, i+1,cursum + candidates[i]) # 从i+1算起
                path.pop()
        dfs(candidates,[],0,0)        
        return res
```





### \216. Combination Sum III

`nums = [1,2,3,4,5,6,7,8,9]`

每个元素最多只用1次，

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k>n or n==1 or n>45:
            return []
        nums = [i for i in range(1,10)]
        res = []
        def dfs(nums, startindex, remain, path):
            if len(path)==k:
                if remain==0:
                    res.append(path[:])
                return
            for i in range(startindex,9):                
                if remain< nums[i]:            #这句话再次是重点，用于剪枝 加速算法
                    return                
                path.append(nums[i])
                dfs(nums, i+1, remain-nums[i],path) # 从i+1 算起
                path.pop()
        dfs(nums,0,n,[])
        return res
```





### \377. Combination Sum IV

给出一个都是正整数的数组 `nums`，其中没有重复的数。从中找出所有的和为 `target` 的组合个数。

**一个数可以在组合中出现多次。数的顺序不同则会被认为是不同的组合。**

```python
nums=[1,2,3]
k=4

#结果
[[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]
```



```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0]>target:
            return 0
        res = []
        candidates =sorted( list(set(nums)))
        n = len(candidates)
        def dfs(candidates, remain, path, start):
            if remain ==0:
                res.append(path[:])
            for i in range(start, n):
                if remain < candidates[i]:
                    break
                path.append(candidates[i])
                dfs(candidates, remain -candidates[i], path, start) #从当前start再次算起
                path.pop()
        dfs(candidates, target, [], 0)
        print(res)
        return len(res)
```

