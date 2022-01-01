class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        # dp[i][j] 表示从s[i:j] 是否是一个子序列
        is_palindrome = [[False] * n for _ in range(n)]
        # 将长度为 1 的 dp 值设为真
        for i in range(n):
            is_palindrome[i][i] = True;
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True


        for new_len in range(3, n + 1):
            for left in range(n - new_len + 1):
                right = left + new_len - 1
                if is_palindrome[left + 1][right - 1]==True and s[left] == s[right]:
                        is_palindrome[left][right] = True
        res = 0

        for left in range(n):
            for right in range(left,n):
                if is_palindrome[left ][right]==True:
                    res+=1
        return res
            
                
                
                
        