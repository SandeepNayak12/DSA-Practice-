class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            div = 0
            for num in nums:
                div += math.ceil(num/mid)
            if div <= threshold:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
