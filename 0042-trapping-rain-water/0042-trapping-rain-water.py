class Solution:
    def trap(self, height: List[int]) -> int:
        def leftMax():
            pref = [-1]*len(height)
            pre = -1
            for i in range(len(height)):
                pref[i] = max(pre,height[i])
                pre = pref[i]
            return pref
        def rightMax():
            post = [-1]*len(height)
            pos = -1
            for i in range(len(height)-1,-1,-1):
                post[i] = max(pos,height[i])
                pos = post[i]
            return post
        left = leftMax()
        right = rightMax()
        Sum = 0
        for i in range(len(height)):
            if height[i] < left[i] and height[i]< right[i]:
                Sum += min(left[i],right[i])-height[i]
        return Sum