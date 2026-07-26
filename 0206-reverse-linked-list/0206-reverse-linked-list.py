# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        temp = head
        while temp:
            stk.append(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            temp.val = stk.pop()
            temp = temp.next
        return head
