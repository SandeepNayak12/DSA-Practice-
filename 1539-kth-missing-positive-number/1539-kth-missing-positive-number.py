class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        k = k
        for num in arr:
            if num <= k:
                k+=1
            else:
                break
        return k