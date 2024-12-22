from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        current_level=deque()
        next_level=[]
        temp=[]
        if root==None:
            return []
        
        current_level.append(root)  
        while len(current_level)>0: #[9]
            next_level=[]
            temp=[]
            for value in current_level: 
                temp.append(value.val)
                if value.left!=None:
                    next_level.append(value.left) #[1,14]
                if value.right!=None:
                    next_level.append(value.right)
            
            ans.append(temp)
            current_level=next_level #cur=[9,20],[]
            next_level=[]
            temp=[]
        return ans
