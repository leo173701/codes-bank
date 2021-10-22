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
        self.sequence = 0
        
        if not lists:
            return None
        
        trav = dummy = ListNode(-1)
        heap = []
        for ll in lists:
            if ll:
                self.heappushNode(heap, ll)
                
        while heap:
            node = heappop(heap)[2]
            trav.next = node
            trav = trav.next
            #print(trav.val)
            if trav.next:
                self.heappushNode(heap, trav.next)
                
        return dummy.next
            
    def heappushNode(self, heap, node):
        self.sequence += 1
        heappush(heap, (node.val, self.sequence, node))