class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimal
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            totalHour = 0
            for bananas in piles:
                totalHour += math.ceil(bananas/mid) 
            if totalHour <= h:
                high = mid-1
            else:
                low = mid+1
        return low 

