# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inordernode=[]
    
        def inorder(node):
            if node==None:
                return None
        
            inorder(node.left)
            inordernode.append(node.val)
            inorder(node.right)
        
        
        inorder(root)
        mini = 1e9
        for i in range(1,len(inordernode)):
            mini=min(mini,inordernode[i]-inordernode[i-1])
        
        return mini
        
        