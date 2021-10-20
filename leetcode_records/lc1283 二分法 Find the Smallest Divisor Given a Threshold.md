



lc1283.Find the Smallest Divisor Given a Threshold

二分法 寻找左边边界

```python
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n==threshold:
            return max(nums)
        left = 1
        right = max(nums)+1
        while left<right:
            mid = (right-left)//2+left
            # print("mid = ",mid)
            value = 0
            for i in nums:
                value += math.ceil(i/mid)
            # print("  value = ",value)
            if  value >threshold:
                left = mid+1
            elif     value<threshold:
                right = mid
            else:
                right = mid
        # print("left = ",left, "   right=",right)
        return left                
```

