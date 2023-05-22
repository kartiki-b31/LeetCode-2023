# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        
        if p.val==q.val:
            leftSame=self.isSameTree(p.left,q.left)
            rightSame=self.isSameTree(p.right,q.right)
            if leftSame==True and rightSame==True:
                return True
            else:
                return False
            
        else:
            return False
        
        
        
        