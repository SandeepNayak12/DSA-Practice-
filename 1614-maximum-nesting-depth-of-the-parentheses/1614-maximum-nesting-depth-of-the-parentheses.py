class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        maxCnt = 0
        for ch in s:
            if ch == '(':
                cnt += 1
                maxCnt = max(maxCnt,cnt)
            if ch == ')':
                cnt -= 1
        return maxCnt