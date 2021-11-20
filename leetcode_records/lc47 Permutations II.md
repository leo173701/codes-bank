\47. Permutations II

### 解题思路

- 这道题我们需要使用dfs+回溯的方法来进行求解。
- 我们定义`dfs`函数，使用递归的方法对决策树进行深度优先遍历。对于长度为`n`的数组`nums`，我们一位一位地生成它的排列数组，每深入一层数组长度就加1，遍历到叶节点时生成数组的长度达到`n`，即为我们的答案。
- 由于数组中有重复元素，所以我们在遍历时需要剪枝操作。

### 算法流程

- 首先对数组进行排序，以使得重复元素相邻，这样才能进行剪枝。
- 定义数组used，used[i]表示nums[i]是否已使用过，初始化全为false。数组path，表示从根结点到该节点经过的路径，即当前已生成的数组，初始化为空。数组res存储结果。
- 使用dfs函数进行递归遍历
  - 递归出口：如果path的长度与nums的长度相等，说明已经生成好了排列数组path，那么我们把它的拷贝加入res中。
  - 遍历nums中的每个元素，对于nums[i]
    - 如果path中已经存在，即used[i]为true，跳过
    - 如果它和前一位元素相等，即nums[i-1] == nums[i]，并且前一位元素已经搜索并回溯过了，即!used[i-1]，为了避免生成重复的排列数组，也跳过
    - 排除上述两种情况后，把nums[i]变为true，然后对新生成的path继续送入dfs函数中。
      最后进行回溯操作，即删除path[i]，used[i]变为false。

### 举例说明

- 如图所示，`nums = [1, 2, 2]`，第二个2标记为2'用于区分相同元素。每个节点有`path`和`used`两个属性。
- 首先，在根结点，`path`为`[]`，`used`全为false（图中标为`[0, 0, 0]`）。然后进行dfs遍历，到下一层，先加入元素1，`path`为`[1]`，`used`为`[1, 0,0 ]`。再到下一层，由于1已经使用过了，我们加入元素2，`path`为`[1， 2]`，`used`为`[1, 1,0 ]`。这样，每深一层`path`长度加1。达到最底层的叶节点，`path`为`[1, 2, 2]`，把它加入`res`中。同理，可以得到其他的叶节点。
- 注意，图中标出画叉的地方，代表出现了重复元素而进行剪枝。
- ![图片](https://media-test.jiuzhang.com/media/markdown/images/6/8/9f610cfc-a924-11ea-a74b-0242ac180006.jpg)

### python 写法

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        # print(nums)
        visited = [False]  * n
        def dfs(nums,n,path):
            if len(path)==n:
                res.append(path[:])
            for index, value in enumerate(nums):
                if visited[index]==True:
                    continue
                if index>0 and nums[index]==nums[index-1] and not visited[index-1]:
                    continue
                visited[index]=True
                # path.append(value)
                dfs(nums,n,path + [value])
                # path.pop()
                visited[index]=False
        dfs(nums,n,[])
        return res
```



![image-20211117134618508](C:/Users/leo17/AppData/Roaming/Typora/typora-user-images/image-20211117134618508.png)

```python
# 笨办法，
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False for _ in range(n)]
        def dfs(nums, path, n ):
            if len(path)==n:
                if path not in res: #判断当前path是否一斤出现过，如果没出现，那就加入到结果当中
                    res.append(path[:])
            for index, value in enumerate(nums):
                if visited[index]==True:
                    continue
                visited[index]=True
                path.append(value)
                dfs(nums,path,n)
                path.pop()
                visited[index]=False
        res = []
        dfs(nums, [ ],n)
        return res
```

### java 写法

```java
public class Solution {
    /*
     * @param :  A list of integers
     * @return: A list of unique permutations
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        Deque<Integer> path = new ArrayDeque<>(nums.length);
        // 排序
        Arrays.sort(nums);
        // dfs
        dfs(nums, used, path, res);
        return res;
    }
        private void dfs(int[] nums, boolean[] used, Deque<Integer> path, List<List<Integer>> res) {
        // 叶子节点
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        
        // 非叶节点
        for (int i = 0; i < nums.length; ++i) {
            // 元素已访问过 或者 是重复元素
            if ((used[i]) || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
                continue;
            }
            
            // 在路径添加该节点，递归
            path.addLast(nums[i]);
            used[i] = true;
            dfs(nums, used, path, res);
            // 回溯
            used[i] = false;
            path.removeLast();
        }
    }
}
赞同
8

令狐冲精选
更新于 12/31/2020, 5:46:10 AM
python
python
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result
```

