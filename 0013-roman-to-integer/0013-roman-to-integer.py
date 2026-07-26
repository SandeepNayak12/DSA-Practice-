class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        Sum = 0
        i = 0
        while i<len(s)-1:
            if mp[s[i]]<mp[s[i+1]]:
                Sum += mp[s[i+1]]-mp[s[i]]
                i +=2
            else:
                Sum += mp[s[i]]
                i+=1
        if i == len(s) - 1:
            Sum += mp[s[i]]
        return Sum
                
            
