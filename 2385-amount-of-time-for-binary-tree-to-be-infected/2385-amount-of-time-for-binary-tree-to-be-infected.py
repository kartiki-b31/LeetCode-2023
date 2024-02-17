from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_matrix=defaultdict(list)
        print(adj_matrix)
        queue=[root]
        
        while queue:
            
            node=queue.pop()
            if node.left:
                queue.append(node.left)
                adj_matrix[node.val].append(node.left.val)
                adj_matrix[node.left.val].append(node.val)
            if node.right:
                queue.append(node.right)
                adj_matrix[node.val].append(node.right.val)
                adj_matrix[node.right.val].append(node.val)
        
        
        queue=[(start,0)]
        visited=set()
        visited.add(start)
        
        while queue:
            node, time=queue.pop(0)
            
            for neighbour in adj_matrix[node]:
                if neighbour not in visited:
                    queue.append((neighbour, time+1))
                    visited.add(neighbour)
        return time
                
                
        
        