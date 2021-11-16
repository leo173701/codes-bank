# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        temp = dummy
        
        pq = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq,(node.val, i, node))
        while pq:
            _, index, node = heapq.heappop(pq)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(pq,(node.next.val, index, node.next))
        return dummy.next
            