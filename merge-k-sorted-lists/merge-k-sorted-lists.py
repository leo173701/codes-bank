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
        dummy = ListNode(0)
        temp = dummy
        heap = []
        for index,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val, index, node))
        while heap:
            _, curindex, curnode= heapq.heappop(heap)
            temp.next = curnode
            temp = temp.next
            if curnode.next:
                heapq.heappush(heap,(curnode.next.val, index, curnode.next))
        return dummy.next