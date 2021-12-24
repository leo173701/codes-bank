class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        length = len(primes)
        times = [0] * length
        uglys = [1]
        minlist = [(primes[i] * uglys[times[i]], i) for i in range(len(times))]
        heapq.heapify(minlist)

        while len(uglys) < n:
            umin, min_times = heapq.heappop(minlist)
            times[min_times] += 1
            if umin != uglys[-1]:
                uglys.append(umin)
            heapq.heappush(minlist, (primes[min_times] * uglys[times[min_times]], min_times))

        return uglys[-1]