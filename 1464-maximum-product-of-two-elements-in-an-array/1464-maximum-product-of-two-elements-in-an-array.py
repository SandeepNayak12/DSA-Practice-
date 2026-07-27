class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        largest = 0
        secLargest = 0
        for i in range(len(arr)):
            if arr[i] > largest:
                secLargest= largest
                largest = arr[i]
            elif arr[i]>secLargest:
                secLargest = arr[i]
        return (secLargest-1)*(largest-1)
