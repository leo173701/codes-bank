class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        bank = set(bank)
        q = deque()
        q.append((start, 0))
        while q:
            seq, step = q.popleft()
            if seq == end:
                return step
            for c in "ACGT":
                for i in range(8):
                    new_seq = seq[:i] + c + seq[i + 1:]
                    if new_seq in bank:
                        q.append((new_seq, step + 1))
                        bank.remove(new_seq)
        return -1