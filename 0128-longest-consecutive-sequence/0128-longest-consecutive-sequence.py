class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # optimal
        s = set(nums)
        longest = 0
        for num in s:
            if num-1 not in s:
                cur = num
                cnt = 1
                while cur+1 in s:
                    cnt+=1
                    cur+=1
                longest = max(longest,cnt)
        return longest