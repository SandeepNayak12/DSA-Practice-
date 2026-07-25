class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        common = ""
        for i in range(len(ref)):
            for word in strs:
                if len(word)<= i or word[i]!=ref[i]:
                    return common
                     
            common+=ref[i]
        return common


