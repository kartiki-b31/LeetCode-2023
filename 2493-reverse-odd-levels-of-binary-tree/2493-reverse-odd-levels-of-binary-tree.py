# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=[]
        current_level=deque()
        next_level=[]
        temp=[]
        level_count=0
        if root==None:
            return []
        #value
        current_level.append(root)  
        while len(current_level)>0: #[9]
            next_level=[]
            temp=[]
            for value in current_level: 
                temp.append(value.val)
                if value.left!=None:
                    #value.left.val=3
                    next_level.append(value.left) #[1,14]
                if value.right!=None:
                    next_level.append(value.right)
            if level_count%2!=0:
                for idx,node in enumerate(current_level):
                    rev_val=temp[::-1]
                    node.val=rev_val[idx]
            ans.append(temp)
            current_level=next_level #cur=[9,20],[]
            next_level=[]
            temp=[]
            level_count+=1
        return root
