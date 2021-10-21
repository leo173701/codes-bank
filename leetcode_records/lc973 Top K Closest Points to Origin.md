

\973. K Closest Points to Origin

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        q = []
        for point in points:
            # print("point = ",point)
            if len(q)<k:
                heapq.heappush(q,(-point[0]*point[0]-point[1]*point[1],point))
            else:
                a = -point[0]*point[0]-point[1]*point[1]
                if q and a>q[0][0]:
                    heapq.heappop(q)
                    heapq.heappush(q,(a,point))
        # return[heapq.heappop(q)[1] for _ in range(k) if q]
        res = []
        for _ in range(k):
            if q:
                temp = heapq.heappop(q)
                res.append(temp[1])
        return res
```

