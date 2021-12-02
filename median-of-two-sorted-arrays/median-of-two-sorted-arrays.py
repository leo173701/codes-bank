class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        m, n = len(A), len(B)
        low, high = 0, m

        while low <= high:
            partition_x = low + (high - low) // 2
            partition_y = (m + n + 1)// 2 - partition_x
            
            # if partition_x is 0 it means nothing is there on left side. Use -INF for max_left_x
            if partition_x == 0:
                max_left_x = float('-inf')
            else:
                max_left_x = A[partition_x - 1]
            
            # if partition_x is length of input then there is nothing on right side. Use +INF for min_right_x
            if partition_x == m:
                min_right_x = float('inf')
            else:
                min_right_x = A[partition_x]
            
            if partition_y == 0:
                max_left_y = float('-inf')
            else:
                max_left_y = B[partition_y - 1]
            
            if partition_y == n:
                min_right_y = float('inf')
            else:
                min_right_y = B[partition_y]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Now get max of left elements and min of right elements to get the median in case of even length combined array size
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                # or get max of left for odd length combined array size.
                else:
                    return max(max_left_x, max_left_y)
            # we are too far on right side for partitionX. Go on left side. 
            elif max_left_x > min_right_y:
                high = partition_x - 1
            # we are too far on left side for partitionX. Go on right side.
            else:
                low = partition_x + 1
        return 0