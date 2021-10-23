class Solution(object):
    def reorganizeString(self, S):
        """
        :type s: str
        :rtype: str
        """
        cnt = collections.Counter(S)
        ans = '#'
        while cnt:
            stop = True
            for v, c in cnt.most_common():
                if v != ans[-1]:
                    stop = False
                    ans += v
                    cnt[v] -= 1
                    if not cnt[v]: del cnt[v]
                    break
            if stop: break
        return ans[1:] if len(ans) == len(S) + 1 else ''