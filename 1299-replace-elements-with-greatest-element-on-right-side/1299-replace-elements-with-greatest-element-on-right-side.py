class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lst = [0]*len(arr)
        post = -1
        for i in range(len(arr)-1,-1,-1):
            lst[i] = post
            post = max(post,arr[i])
        return lst