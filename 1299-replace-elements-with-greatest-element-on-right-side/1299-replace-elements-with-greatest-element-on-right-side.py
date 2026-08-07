class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        post = -1
        for i in range(len(arr)-1,-1,-1):
            cur = arr[i]
            arr[i] = post
            post = max(post,cur)
        return arr