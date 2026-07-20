class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        minDay = 0
        while low<=high:
            mid = (low+high)//2
            cnt = 0
            noOfBouque = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    cnt+=1
                    if cnt == k:
                        noOfBouque +=1
                        cnt = 0
                else:
                    cnt = 0
            if noOfBouque >= m:
                minDay = mid
                high = mid-1
            else:
                low = mid+1
        return minDay
        
            