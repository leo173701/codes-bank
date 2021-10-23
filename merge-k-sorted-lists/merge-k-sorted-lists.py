# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        tail, heap = dummy, []
        
        for index, head in enumerate(lists):
            if not head: continue
            heappush(heap, (head.val, index, head))
            
        while heap:
            _, index, head = heappop(heap)
            tail.next, tail = head, head
            if head.next:
                heappush(heap, (head.next.val, index, head.next))
                
        return dummy.next