# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carrie = 0
        cur = dummy

        while(l1 or l2 or carrie):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a+b+carrie
            carrie = 1 if sum>9 else 0
            val = sum%10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next 