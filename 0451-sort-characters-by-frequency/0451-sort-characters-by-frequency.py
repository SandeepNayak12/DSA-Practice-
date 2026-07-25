class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        result = ""
        for ch in s:
            mp[ch] = mp.get(ch,0)+1
        sortValues = sorted(mp.items(),key = lambda x : x[1], reverse = True)
        for key,value in sortValues:
            result += key*value

        return result
        