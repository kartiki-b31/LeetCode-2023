# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        q=deque()
        level=[]
        max_ele=0
        level2=[]
        q.append(root)
        res=[]
        res.append(root.val)

        while q:
            level=[]
            level2=[]
            for current in q:
                if current.left:
                    level.append(current.left)
                    level2.append(current.left.val)
                if current.right:
                    level.append(current.right)
                    level2.append(current.right.val)
            
            if len(level2)>0: 
                max_ele=max(level2)
                res.append(max_ele)
            q=level
        
        return res


