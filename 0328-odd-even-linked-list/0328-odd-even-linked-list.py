# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        arr = []
        temp = head
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        temp = head.next
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        temp = head
        i = 0
        while temp and i<len(arr):
            temp.val = arr[i]
            temp = temp.next
            i+=1
        return head