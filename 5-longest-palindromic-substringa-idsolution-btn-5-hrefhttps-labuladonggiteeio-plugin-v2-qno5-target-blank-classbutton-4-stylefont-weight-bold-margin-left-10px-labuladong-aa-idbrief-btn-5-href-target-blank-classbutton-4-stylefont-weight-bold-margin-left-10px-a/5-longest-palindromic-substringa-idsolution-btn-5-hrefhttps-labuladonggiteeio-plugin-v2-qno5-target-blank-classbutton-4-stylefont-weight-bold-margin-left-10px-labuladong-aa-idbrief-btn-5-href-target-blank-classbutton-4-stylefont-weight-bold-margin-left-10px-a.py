class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_len = 1
        start = 0
        is_palindrome = [[False] * length for _ in range(length)]
        
        # 将长度为 1 的 dp 值设为真
        for i in range(length):
            is_palindrome[i][i] = True;
        
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                max_len = 2
                start = i
        
        for new_len in range(3, length + 1):
            for left in range(length - new_len + 1):
                right = left + new_len - 1
                if is_palindrome[left + 1][right - 1] and s[left] == s[right]:
                    is_palindrome[left][right] = True
                    # 更新答案
                    if new_len > max_len:
                        max_len = new_len
                        start = left
        
        return s[start : start + max_len]