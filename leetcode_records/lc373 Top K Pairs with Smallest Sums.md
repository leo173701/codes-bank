

\373. Find K Pairs with Smallest Sums

思路： top k smallest 用最大堆，

​             top k largest   用最小堆。

```python
    def kSmallestPairs(self, nums1, nums2, k):
        q = []
        for i in nums1:
            for j in nums2:
                if len(q)<k:
                    heapq.heappush(q, (-i-j,[i,j]))   # python默认最小堆，所以需要使用负数
                else:
                    if q and i+j<-q[0][0]:
                        # print(q)
                        heapq.heappop(q)
                        heapq.heappush(q,(-i-j,[i,j]))
                    else: 
                        break   #这一步极大地降低了时间消耗
        return [heapq.heappop(q)[1] for _ in range(k) if q]
```

