class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        pref = []
        for i in range(len(nums)):
            pre+=nums[i]
            pref.append(pre)
        pos = 0
        post = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            pos+=nums[i]
            post[i]=pos
 
        for i in range(len(nums)):
            if pref[i]==post[i]:
                return i
        return -1
