# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if p==None and q==None:
                return True
            if p==None or q==None:
                return False
        
            if p.val==q.val:
                leftSame=isSame(p.left,q.right)
                rightSame=isSame(p.right,q.left)
                if leftSame==True and rightSame==True:
                    return True
                else:
                    return False
            
            else:
                return False
        return isSame(root.left,root.right)
        