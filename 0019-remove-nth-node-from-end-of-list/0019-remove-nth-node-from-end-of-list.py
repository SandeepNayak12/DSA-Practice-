# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # BF
        if not head:
            return None
        cnt = 0
        temp = head
        while temp:
            cnt+=1
            temp = temp.next
        temp = head
        n = cnt-n
        if n==0:
            return head.next
        for i in range(n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head

