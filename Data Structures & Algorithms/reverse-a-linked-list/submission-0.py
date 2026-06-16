# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, root: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        cur = root

        while(cur):
            temp = cur.next
            cur.next=prev
            prev = cur
            cur = temp
        return prev