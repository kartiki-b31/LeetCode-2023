# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        q=deque()
        visited=set()
        max_ele=0
        res=[]
        ans=0
        arr=[]

        def bfs(node,level):
            if len(arr)<level:
                arr.append(float('-inf'))
            arr[level-1]=max(arr[level-1],node.val)
            if node.left:
                bfs(node.left,level+1)

            if node.right:
                bfs(node.right,level+1)   
                
        bfs(root,1)

        return arr
