

\31. Next Permutation

https://leetcode.com/problems/next-permutation/

### 要求

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。



### 思路

从最后一个位置开始，找到一个上升点，上升点之前的无需改动。 （4<6 所以4是目标值）

从右往左遍历，找到一个可以替换的点，然后保证用点右边比它大的点中最小的那个和它替换。 然后再保证点右边是升序的，就完成了下一个序列 

在4右手边找比它大的最小那个数也就是5，

 45交换位置得到125643

在原来4所在的位置的右侧643，做排序得到最小值

![image-20211117152240395](lc31%20Next%20Permutation.assets/image-20211117152240395.png)





```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2:
            return nums
        loc = n-2
        while nums[loc+1]<=nums[loc] and loc>=0:
            loc-=1
        # print("loc = ", loc)
        # print(nums[loc], nums[loc+1])
        minvalue = nums[loc+1]
        targetlocation = loc+1
        for i, value in enumerate(nums[loc:]):
            if value > nums[loc]:
                if value < minvalue:
                    minvalue = value
                    targetlocation = i + loc
        # print("minvalue = ",minvalue)
        # print("targetlocation = ",targetlocation)
        nums[loc], nums[targetlocation] =  nums[targetlocation],nums[loc]
        # print(nums)
        a = loc+1
        nums[:]=nums[:a] + sorted(nums[a:])
```

