class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mpS = {}
        mpT = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if charS in mpS:
                if mpS[charS]!=charT:
                    return False
            if charT in mpT:
                if mpT[charT]!= charS:
                    return False
        
            mpS[charS] = charT
            mpT[charT] = charS
        return True

        