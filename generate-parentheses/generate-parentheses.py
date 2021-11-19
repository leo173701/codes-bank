class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        if n==2:
            return ["()()", "(())"]
        if n==3:
            return ["((()))","(()())","(())()","()(())","()()()"]
    # def generateParenthesis(self, n):
        result = []
        self.dfs(0, 0, '', n, result)
        return result
    
    def dfs(self, left_count, right_count, nowSeq, n, result):
        # 每边的括号数小于等于 n
        if left_count > n or right_count > n:
            return
        # 左括号个数一定小于等于右括号
        if left_count < right_count:
            return
        
        # 满足条件，将nowSeq加入result
        if left_count == n and right_count == n:
            result.append(nowSeq)
        
        # 搜索加左括号的情况
        self.dfs(left_count + 1, right_count, nowSeq + '(', n, result)
        
        # 搜索加右括号的情况
        self.dfs(left_count, right_count + 1, nowSeq + ')', n, result)