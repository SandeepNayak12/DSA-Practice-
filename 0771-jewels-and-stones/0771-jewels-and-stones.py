class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt=0
        for ch in stones:
            if ch in jewels:
                cnt+=1
        return cnt
