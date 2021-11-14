# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        
        graph = defaultdict(set)
        self.dfs(None, root, graph)
        q=deque([target])
        current_distance = 0
        visited = {target}
        while q:
            next_level = deque([])
            if current_distance==K:
                break
            while q:
                cur = q.popleft()
                for node in graph[cur]:
                    if node in visited:
                        continue
                    visited.add(node)
                    next_level.append(node)
            q=next_level
            current_distance +=1
        # print([node.val for node in q])
        return [node.val for node in q]
            
            
            
    def dfs(self,parent, node, graph):
        if not node:
            return
        if parent and node:
            graph[node].add(parent)
            graph[parent].add(node)
        if node.left:
            self.dfs(node,node.left, graph)
        if node.right:
            self.dfs(node,node.right,graph)
        
        
        
              