class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        ans = []
        for candi in candies:
            if candi + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
        return ans