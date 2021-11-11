class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        bankset = set(bank)
        q = deque([])
        q.append((start,0))
        while q:
            cur, step = q.popleft()
            if cur ==end:
                return step
            for char in "ACGT":
                for i in range(8):
                    mutation = cur[:i]+char + cur[i+1:]
                    if mutation in bankset:
                        q.append((mutation,step+1))
                        bankset.remove(mutation)
        return -1