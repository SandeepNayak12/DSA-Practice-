class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == '(' or ch =='[' or ch=='{':
                stk.append(ch)
            else:
                if not stk:
                    return False
                if ch == ')':
                    if stk.pop() != '(':
                        return False
                if ch == ']':
                    if stk.pop() != '[':
                        return False
                if ch =='}':
                    if stk.pop()!= '{':
                        return False
        if stk:
            return False
        else:
            return True   
