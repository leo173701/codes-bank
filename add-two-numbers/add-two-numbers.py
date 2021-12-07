# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0 
        while l1 or l2 or carry:
            number = 0
            if l1:
                number +=l1.val
                l1=l1.next
            if l2:
                number +=l2.val
                l2=l2.next
            number +=carry
            digit, carry = number%10, number//10
            node = ListNode(digit)
            temp.next = node
            temp = temp.next
        return dummy.next