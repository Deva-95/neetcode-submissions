# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head1 = head
        head2 = head
        i = 1
        prev = head2
        while(head1.next and i<n):
            i+=1
            head1=head1.next
        
        while(head1.next):
            prev = head2
            head2 = head2.next
            head1 = head1.next
        
        if head2 == head:return head.next
        prev.next = head2.next
        return head