class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        result = ""
        for char in s:
            if char =='(':
                if cnt > 0:
                    result +=char
                cnt+=1
            else:
                cnt-=1
                if cnt > 0:
                    result += char
                    
        return result