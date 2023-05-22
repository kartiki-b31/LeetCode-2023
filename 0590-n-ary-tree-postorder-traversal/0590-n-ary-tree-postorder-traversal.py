"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.arr=[]
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return None
        for i in range(len(root.children)):
            self.postorder(root.children[i])
        self.arr.append(root.val)
        
        return self.arr
        
        