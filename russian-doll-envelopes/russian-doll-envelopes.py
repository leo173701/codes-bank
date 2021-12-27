class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        # if n==1: 
        #     return 1
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # 初始化dp数组，cnt表示dp数组长度
        # 令dp[i] = minwidth表示长度为i的上升子序列的结尾的元素的width最小是为minwidth
        dp = []
        cnt = 0
        envelopesLen = len(envelopes)
        for i in range(envelopesLen):
            # 使用bisect_left二分查找函数，返回第一个大于等于envelopes[i][1]的值，如果没有 返回dp数组长度
            idx = bisect.bisect_left(dp, envelopes[i][1])
            # 没有找到，直接添加到末尾
            if idx == cnt:
                cnt += 1
                dp.append(envelopes[i][1])
            # 找到了，进行优化
            else:
                dp[idx] = envelopes[i][1]
        # dp数组长度就是答案
        return cnt