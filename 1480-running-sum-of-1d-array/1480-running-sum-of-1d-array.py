class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        Sum = 0
        for num in nums:
            Sum +=num
            ans.append(Sum)
        return ans