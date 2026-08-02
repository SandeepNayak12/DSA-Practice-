class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        postf = [1]*len(nums)
        ans = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            pref[i] = pre
            pre = pre*nums[i]

        post = 1
        for i in range(len(nums)-1,-1,-1):
            postf[i] = post
            post = post*nums[i]


        for i in range(len(nums)):
            ans[i] = postf[i]*pref[i]
        return ans