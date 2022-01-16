# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



#Better Memory use
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n

        return prev

#Better Speed
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
