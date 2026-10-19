# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        head1 = list1
        head2 = list2

        dummy = ListNode()
        tail = dummy

        while head1 is not None  and head2 is not None:

            if head1.val <= head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next
            
        tail.next = head1 or head2

        return dummy.next
