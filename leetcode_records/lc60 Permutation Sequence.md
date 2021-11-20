\60. Permutation Sequence



```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1:
            return "1"
        factory = []
        temp =1
        nums = []
        
        for i in range(1,n):
            nums.append(i)
            temp *=i
            factory.append(temp)
        nums.append(n)
        res = ""
        i=1
        while i<n:
            solution, remainder = k//factory[-i], k%factory[-i] 
            # print("solution = ",solution)
            # print("remainder = ",remainder)
            if solution!=0 :
                if remainder!=0:
                    a = nums[solution]
                    res +=str(a)
                    i +=1
                    k = remainder
                    nums.remove(a)
                    # print("nums = ",nums)
                else:
                    a = nums[solution-1]
                    res +=str(a)
                    nums.remove(a)
                    nums.sort(reverse = True)
                    for m in nums:
                        res +=str(m)
                    # print("nums = ",nums)
                    return res
            else:
                a = nums[solution]
                res +=str(a)
                i +=1
                k = remainder
                nums.remove(a)
                # print("nums = ",nums)
        return res
```





```python
# 笨办法
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # n = len(nums)
        visited = []
        nums=[]
        for i in range(1,n+1):
            visited.append(False)
            nums.append(i)
        # nums = [i for i in range(1,n+1)]
        # visited = [False for _ in range(n)]
        res = []
        def dfs(nums, n, path):
            if len(path)==n:
                res.append(path[:])
            if len(res)==k:
                return
            for index,value in enumerate(nums) :
                if visited[index]==True:
                    continue
                visited[index]=True
                # path.append(value)
                dfs(nums,n,path+[value])
                # path.pop()
                visited[index]=False
        dfs(nums,n,[])
        a = ""
        for i in range(n):
            a+=str(res[-1][i])
        return a
```

