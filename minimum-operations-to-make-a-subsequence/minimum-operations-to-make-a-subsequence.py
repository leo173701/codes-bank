class Solution:
    def minOperations(self, target : List[int], A: List[int]) -> int:            
        ha = {a: i for i, a in enumerate(target)}
        stack = []
        for a in A:
            if a not in ha: continue
            i = bisect.bisect_left(stack, ha[a])
            if i == len(stack):
                stack.append(0)
            stack[i] = ha[a]
        return len(target) - len(stack)