class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0
        h = len(nums)-1
        while l<=h:
            if nums[l] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                i+=1
                l+=1
            elif nums[l]== 1:
                l+=1
            else:
                nums[l],nums[h] = nums[h],nums[l]
                h-=1
