# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[]
        q.append(root)
        res=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.pop(0)
                if node:
                    level.append(node.val)
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            if level:
                res.append(sum(level)/len(level))
        return res
