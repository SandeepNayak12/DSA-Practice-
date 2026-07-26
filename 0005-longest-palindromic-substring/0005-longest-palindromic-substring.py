class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left,right):
            while left>=0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return left+1,right-left-1

        start = 0
        maxLen = 0
        
        for i in range(len(s)):
            # odd
            left1,len1 = expand(i,i)
            if len1>maxLen:
                start = left1
                maxLen = len1

            # even
            left2,len2 = expand(i,i+1)
            if len2>maxLen:
                start = left2
                maxLen = len2
        return s[start:start+maxLen]