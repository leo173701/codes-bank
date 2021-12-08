class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort(reverse= True)
        maxDay = days[0]
        passDays = [1, 7, 30]
        f = [0] + [1000000] * maxDay 
        
        for j in range(1, maxDay + 1): 
            if j not in days: 
                f[j] = f[j - 1]
            else: 
                f[j] = min(f[j], f[max(j - 1, 0)] + costs[0], f[max(j - 7, 0)] + costs[1], f[max(j - 30, 0)] + costs[2])
        
        
        return f[maxDay]