例题：\34. Find First and Last Position of Element in Sorted Array
找到从左边开始的第一个元素，和从右边开始的第一个元素


### 1. 二分标准模板 

```java
//Java
public int binarySearch(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;                     // 左右都闭合的区间 [l, r]
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid;
        if (nums[mid] < target)
            left = mid + 1;                          // 解空间变为 [mid+1, right]
        if (nums[mid] > target)
            right = mid - 1;                         // 解空间变为 [left, mid - 1]
    }
    return -1;
}
```



```python
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1            # 左右都闭合的区间 [l, r]
    while l <= r:
        mid = (left + right) >> 1
        if nums[mid] == target: 
            return mid      
        if nums[mid] < target: 
            l = mid + 1       # 解空间变为 [mid+1, right] 
        if nums[mid] > target: 
            r = mid - 1       # 解空间变为 [left, mid - 1]
    return -1
```



### 2. 寻找最左插入位置

具体算法：

首先定义解空间为 [left, right]，注意是左右都闭合，之后会用到这个点。

由于我们定义的解空间为 [left, right]，因此当 left <= right 的时候，解空间都不为空。 也就是说我们的终止搜索条件为 left <= right。

当 A[mid] >= x，**满足题意**，我们令 `right = mid - 1` 将 mid 从解空间排除，继续看看有没有更好的备胎。

当 A[mid] < x，说明 mid 根本就不是答案，直接更新 `left = mid + 1`，从而将 mid 从解空间排除。

最后解空间的 left 就是最好的备胎，备胎转正。

```python
# 找比 x 小的第一个元素
def bisect_left(nums, x):   
    bisect.bisect_left(nums, x)         # 内置 api
   
    l, r = 0, len(A) - 1                # 手写
    while l <= r:
        mid = (l + r) // 2
        if A[mid] >= x: 
            r = mid - 1
        else: 
            l = mid + 1
    return l
```

### 3. 寻找最右插入位置

具体算法：

首先定义解空间为 [left, right]，注意是左右都闭合，之后会用到这个点。

由于我们定义的解空间为 [left, right]，因此当 left <= right 的时候，解空间都不为空。 也就是说我们的终止搜索条件为 left <= right。

当 A[mid] <= x，**满足题意**，我们令 `left = mid + 1` 将 mid 从解空间排除，继续看看有没有更好的备胎。

当 A[mid] > x，说明 mid 根本就不是答案，直接更新 `right = mid - 1`，从而将 mid 从解空间排除。

最后解空间的 right 就是最好的备胎，备胎转正。 return right

```python
# 找比 x 大的第一个元素
def bisect_left(nums, x):   
    bisect.bisect_right(nums, x)         # 内置 api
   
    l, r = 0, len(A) - 1                # 手写
    while l <= r:
        mid = (l + r) // 2
        if A[mid] <= x: 
            l = mid + 1
        else: 
            r = mid - 1
    return r
```



例题：\34. Find First and Last Position of Element in Sorted Array

找到从左边开始的第一个元素，和从右边开始的第一个元素

```python
def searchRange(self, nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) >> 1         
            if x <= A[mid]: 
                right = mid-1
            else: 
                left = mid+1            #从左边第一个
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) >>1      
            if x >= A[mid]:             # 从右边的第一个
                left = mid + 1
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    if left <= right:
        return (left, right)
    else:
        [-1, -1]
```

