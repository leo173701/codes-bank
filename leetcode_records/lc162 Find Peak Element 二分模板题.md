\162. Find Peak Element 二分模板题



参考： https://leetcode.com/problems/find-peak-element/discuss/1290642/Intuition-behind-conditions-or-Complete-Explanation-or-Diagram-or-Binary-Search



Case 1 : mid lies on the right of our result peak ( Observation : Our peak element search space is leftside )
Case 2 : mid is equal to the peak element ( Observation : mid element is greater than its neighbors )
Case 3 : mid lies on the left. ( Observation : Our peak element search space is rightside )



so, the code becomes

![image](https://assets.leetcode.com/users/images/d2fdc688-542e-434c-8969-f151b2286313_1624387000.3221495.png)

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:    
    	if len(nums)==1:
            return 0
        n = len(nums)
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        left = 1
        right = n-2
        while left<=right:
            mid = (right+left)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid-1]:
                right = mid-1
            elif nums[mid]<nums[mid+1]:
                left = mid+1
        return -1
```

```java
class Solution {
    public int findPeakElement(int[] nums) {		
		if(nums.length == 1) return 0; // single element
        
        int n = nums.length;
        
		// check if 0th/n-1th index is the peak element
        if(nums[0] > nums[1]) return 0;
        if(nums[n-1] > nums[n-2]) return n-1;
		
		// search in the remaining array
        int start = 1;
        int end = n-2;
        
        while(start <= end) {
            int mid = start + (end - start)/2;
            if(nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1]) return mid;
            else if(nums[mid] < nums[mid-1]) end = mid - 1;
            else if(nums[mid] < nums[mid+1]) start = mid + 1;
        }
        return -1; // dummy return statement
    }
}
```

