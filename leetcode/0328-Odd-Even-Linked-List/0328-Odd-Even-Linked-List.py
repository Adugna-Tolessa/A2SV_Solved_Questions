# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        evens = head.next
        e_head = evens
        while evens and evens.next:
            cur.next = evens.next
            cur = cur.next

            evens.next = cur.next
            evens = cur.next
            
        
        cur.next = e_head
        return head