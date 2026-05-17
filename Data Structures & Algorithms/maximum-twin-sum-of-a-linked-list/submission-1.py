# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # now we have slow at half way and fast at the end
        # let's reverse the tail end!
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # cur is now null, 2nd half is now reversed
        # set new pointers 1 at head 1 at prev (start of reversed one)
        # add em up
        fwd = head
        bwd = prev
        maxSum = 0
        while bwd:
            maxSum = max(maxSum, fwd.val + bwd.val)
            fwd = fwd.next
            bwd = bwd.next
        return maxSum
            
            

