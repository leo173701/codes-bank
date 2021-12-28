class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if A == None or len(A) < 3:
            return 0
        N = len(A)
        f = [{} for _ in range(N)]
        f2 = [{} for _ in range(N)]
        
        ans = 0
        for i in range(N):
            for j in range(i):
                d = A[i] - A[j]
                
                if d in f2[i]:
                    f2[i][d] += 1 
                else:
                    f2[i][d] = 1 
                
                f2_j_d = f2[j][d] if d in f2[j] else 0
                f_j_d = f[j][d] if d in f[j] else 0
                f_i_d = f[i][d] if d in f[i] else 0
                f[i][d] = f_i_d + f_j_d + f2_j_d
            for d in f[i]:
                ans += f[i][d]
        return ans
                
                