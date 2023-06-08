# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def inorder(root):
            nonlocal ans
            if root==None:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
            return
        
        inorder(root)
        return ans == sorted(set(ans))
            
                 
        

        
            
        
        
        