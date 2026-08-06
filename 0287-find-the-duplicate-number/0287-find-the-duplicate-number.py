class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        seen = set()
        for num in arr:
            if num in seen:
                return num
            else:
                seen.add(num)