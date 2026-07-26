class Solution:
    def beautySum(self, s: str) -> int:
        Sum = 0
        for i in range(len(s)):
            mp = {}
            for j in range(i,len(s)):
                mp[s[j]] = mp.get(s[j],0)+1
                maxi = max(mp.values())
                mini = min(mp.values())
                Sum += maxi-mini
        return Sum