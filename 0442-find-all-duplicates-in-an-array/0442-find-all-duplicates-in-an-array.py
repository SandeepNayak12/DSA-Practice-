class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp = {}
        ans = []
        for num in nums:
            mp[num] = mp.get(num,0)+1
        for key,value in mp.items():
            if value == 2:
                ans.append(key)
        return ans
