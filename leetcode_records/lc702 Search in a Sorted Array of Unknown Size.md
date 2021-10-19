

[702. Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size)

先去缩小范围

```PYTHON
def search(nums, target):
    right = 1
    while(nums[right] < target):
        right =2*right
    left = right>>1
    while left<=right:
        mid = left + (right-left)//2
        val =nums[mid]
        if val==target:
            return mid
        elif val>nums[left]:
            right = mid-1
        else:
            left = mid+1
    return -1
```

