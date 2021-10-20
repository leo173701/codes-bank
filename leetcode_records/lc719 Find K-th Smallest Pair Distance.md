lc 719. Find K-th Smallest Pair Distance
思路总结：

1. 对数组进行排序
2. low = 0, high = nums[-1] - nums[0] (也就是最大值减去最小值， 自然得到最大差值)
3. 进行二分搜索， 这里需要特别注意怎么引入 k的

```java
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length, low = 0, hi = nums[n-1] - nums[0];
        while (low < hi) {
            int cnt = 0, j = 0, mid = (low + hi)/2;
            for (int i = 0; i < n; ++i) {
                while (j < n && nums[j] - nums[i] <= mid) ++j;
                cnt += j - i-1;
            }
            if (cnt >= k) 
                hi = mid;
            
            else low = mid + 1;
        }
        
        return low;
    }
}
```